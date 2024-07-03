import requests
import time

import vertexai

from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Part,
    Tool,
)

def generate_function_call(prompt: str, project_id: str, location: str) -> tuple:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)

    # Initialize Gemini model
    model = GenerativeModel("gemini-1.0-pro-001")

    # Specify a function declaration and parameters for an API request
    get_current_weather_func = FunctionDeclaration(
        name="get_current_weather",
        description="Get the current weather in a given location",
        # Function parameters are specified in OpenAPI JSON schema format
        parameters={
            "type": "object",
            "properties": {"location": {"type": "string", "description": "Location"}},
        },
    )

    # Define a tool that includes the above get_current_weather_func
    weather_tool = Tool(
        function_declarations=[get_current_weather_func],
    )

    # Define the user's prompt in a Content object that we can reuse in model calls
    user_prompt_content = Content(
        role="user",
        parts=[
            Part.from_text(prompt),
        ],
    )

    # Send the prompt and instruct the model to generate content using the Tool that you just created
    response = model.generate_content(
        user_prompt_content,
        generation_config=GenerationConfig(temperature=0),
        tools=[weather_tool],
    )
    response_function_call_content = response.candidates[0].content

    # Check the function name that the model responded with, and make an API call to an external system
    if (
        response.candidates[0].content.parts[0].function_call.name
        == "get_current_weather"
    ):
        # Extract the arguments to use in your API call
        location = (
            response.candidates[0].content.parts[0].function_call.args["location"]
        )
        print('location', location)

        weather_api_url = "https://function-calling-phdovlv6aa-du.a.run.app/get-weather"

        # Here you can use your preferred method to make an API request to fetch the current weather, for example:
        response = requests.post(weather_api_url, data={"location": location})
        print('api_response', response.content)
        api_response = response.content

        # In this example, we'll use synthetic data to simulate a response payload from an external API
        #api_response = """{ "location": "Boston, MA", "temperature": 38, "description": "Partly Cloudy",
        #                "icon": "partly-cloudy", "humidity": 65, "wind": { "speed": 10, "direction": "NW" } }"""
        #api_response = """{ "location": "경기도 수원시", "temperature": 38, "description": "Partly Cloudy",
        #                "icon": "partly-cloudy", "humidity": 65, "wind": { "speed": 10, "direction": "NW" } }"""

    # Return the API response to Gemini so it can generate a model response or request another function call
    response = model.generate_content(
        [
            user_prompt_content,  # User prompt
            response_function_call_content,  # Function call response
            Content(
                parts=[
                    Part.from_function_response(
                        name="get_current_weather",
                        response={
                            "content": api_response,  # Return the API response to Gemini
                        },
                    )
                ],
            ),
        ],
        tools=[weather_tool],
    )
    # Get the model summary response
    summary = response.candidates[0].content.parts[0].text

    return summary, response

PROJECT_ID = "tpcg-datacollector"
REGION = "asia-northeast3"

summary, response = generate_function_call(
    prompt="서울 날씨를 가르쳐 줘", 
    project_id=PROJECT_ID, 
    location=REGION
)
print(summary)
print(response)