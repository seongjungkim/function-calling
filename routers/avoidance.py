
import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

import routers.prompts as prompts

def generate_avoidance(question):
    #https://ai.google.dev/api/generate-content?hl=ko#text
    prompt = prompts.avoidance_prompt + f"""{question}"""
    print('prompt', prompt)

    PROJECT_ID = "samsung-poc-425503"
    LOCATION = "asia-northeast3"
    vertexai.init(project=PROJECT_ID, location=LOCATION)

    model_name = "gemini-1.5-flash-001"
    model = GenerativeModel(model_name)

    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

    safety_settings = {
        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }

    try:
        response = model.generate_content(
            [prompt],
            generation_config=generation_config,
            safety_settings=safety_settings,
            #stream=True,
        )

        print(response.text)
        return response.text
    except Exception as e:
        print(e)

    return None
