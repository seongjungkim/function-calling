import json
import requests
import vertexai

from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Part,
    Tool,
    ToolConfig,
)

#https://colab.research.google.com/drive/1hySdEtHY_6-rkdoovmzL_4XoTT-VxXxg?resourcekey=0-Y-byjubldalGDutCVNEheA#scrollTo=TUFi7L8lCscV

def generate_function_call(prompt: str, project_id: str, location: str) -> tuple:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)

    # Initialize Gemini model
    model_type = "gemini-1.5-pro-001"
    #model_type = "gemini-1.5-flash-001"
    model = GenerativeModel(model_type)

    """
    gemini-1.5-flash-001
    google.api_core.exceptions.InvalidArgument: 400 Unable to submit request because the forced function calling (mode = ANY) is only supported for Gemini 1.5 Pro models. Learn more: https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling
    """

    # Specify a function declaration and parameters for an API request
    get_galaxy_spec_func = FunctionDeclaration(
        name="get_galaxy_spec",
        description="Get the specification in Galaxy Smartphone",
        # Function parameters are specified in OpenAPI JSON schema format
        parameters={
            "type": "object",
            "properties": {
                "model": {"type": "array", "description": "Product model(s)"},
                "category": {"type": "string", "description": "제품 스펙 항목"},
            },
        },
    )
    compare_galaxy_spec_func = FunctionDeclaration(
        name="compare_galaxy_spec",
        description="Compare specifications between Galaxy Series",
        # Function parameters are specified in OpenAPI JSON schema format
        parameters={
            "type": "object",
            "properties": {
                "model": {"type": "array", "description": "Product model(s)"},
                "comparison": {"type": "string", "description": "Comparison Category"},
            },
        },
    )

    # Define a tool that includes the above get_current_weather_func
    galaxy_tool = Tool(
        function_declarations=[
            get_galaxy_spec_func,
            compare_galaxy_spec_func,
        ],
    )

    # Define the user's prompt in a Content object that we can reuse in model calls
    user_prompt_content = Content(
        role="user",
        parts=[
            Part.from_text(prompt),
        ],
    )

    tool_config = ToolConfig(
        function_calling_config=ToolConfig.FunctionCallingConfig(
            # ANY mode forces the model to predict a function call
            mode=ToolConfig.FunctionCallingConfig.Mode.ANY,
            # Allowed functions to call when the mode is ANY. If empty, any one of
            # the provided functions are called.
            #allowed_function_names=["get_galaxy_spec", "compare_galaxy_spec"],
        )
    )

    tool_config = ToolConfig(
        function_calling_config=ToolConfig.FunctionCallingConfig(
            #mode=ToolConfig.FunctionCallingConfig.Mode.AUTO,  # The default model behavior. The model decides whether to predict a function call or a natural language response.
            mode=ToolConfig.FunctionCallingConfig.Mode.ANY,
        )
    )

    # Send the prompt and instruct the model to generate content using the Tool that you just created
    response = model.generate_content(
        user_prompt_content,
        generation_config=GenerationConfig(temperature=0),
        tools=[galaxy_tool],
        #tool_config=tool_config,
    )
    response_function_call_content = response.candidates[0].content

    # Check the function name that the model responded with, and make an API call to an external system
    function_call_type = response.candidates[0].content.parts[0].function_call.name

    #TPCG-DataCollector
    #base_api_url = "https://function-calling-phdovlv6aa-du.a.run.app"
    #samsung-poc
    #base_api_url = "https://function-calling-jr6kniykka-du.a.run.app"
    base_api_url = "https://dialogflow-fulfillment-jr6kniykka-du.a.run.app"
    #base_api_url = "http://localhost:8080"

    print('prompt:', prompt)
    print('function_call_type:', function_call_type)
    if (
        function_call_type == "get_galaxy_spec"
    ):
        # Extract the arguments to use in your API call
        model_id = (
            response.candidates[0].content.parts[0].function_call.args["model"]
        )
        print('model:', model_id)
        try:
            category = (
                response.candidates[0].content.parts[0].function_call.args["category"]
            )
        except KeyError as e:
            category = None
        print('category:', category)

        galaxy_api_url = f"{base_api_url}/galaxy-spec"

        # Here you can use your preferred method to make an API request to fetch the current weather, for example:
        data = {"model": ','.join(model_id)}
        headers = {"Content-Type": "application/json; charset=utf-8"}
        #response = requests.post(galaxy_api_url, data=json.dumps(data))
        response = requests.post(galaxy_api_url, headers=headers, data=json.dumps(data))
        #print('response', response)
        #print('api_response', response.content)
        api_response = response.content

        # In this example, we'll use synthetic data to simulate a response payload from an external API
        #api_response = """{ "location": "Boston, MA", "temperature": 38, "description": "Partly Cloudy",
        #                "icon": "partly-cloudy", "humidity": 65, "wind": { "speed": 10, "direction": "NW" } }"""
        #api_response = "{ '모델코드': { '1': 'SM-S921NLBFKOO' }, '운영체제': {'1': 'Android'} }"
    elif (
        function_call_type == "compare_galaxy_spec"
    ):
        # Extract the arguments to use in your API call
        models = (
            response.candidates[0].content.parts[0].function_call.args["model"]
        )
        print('model:', models)
        try:
            comparison_category = (
                response.candidates[0].content.parts[0].function_call.args["comparison"]
            )
        except KeyError as e:
            comparison_category = None
        print('comparison:', comparison_category)

        galaxy_api_url = f"{base_api_url}/compare-galaxy-spec"

        # Here you can use your preferred method to make an API request to fetch the current weather, for example:
        data = {"model": ','.join(models)}
        headers = {"Content-Type": "application/json; charset=utf-8"}
        #response = requests.post(galaxy_api_url, data=json.dumps(data))
        response = requests.post(galaxy_api_url, headers=headers, data=json.dumps(data))
        #print('response', response)
        print('api_response', response.content)
        api_response = response.content

        # In this example, we'll use synthetic data to simulate a response payload from an external API
        #api_response = """{ "location": "Boston, MA", "temperature": 38, "description": "Partly Cloudy",
        #                "icon": "partly-cloudy", "humidity": 65, "wind": { "speed": 10, "direction": "NW" } }"""
        #api_response = "{ '모델코드': { '1': 'SM-S921NLBFKOO' }, '운영체제': {'1': 'Android'} }"

    # Return the API response to Gemini so it can generate a model response or request another function call
    response = model.generate_content(
        [
            user_prompt_content,  # User prompt
            response_function_call_content,  # Function call response
            Content(
                parts=[
                    Part.from_function_response(
                        name=function_call_type,
                        response={
                            "content": api_response,  # Return the API response to Gemini
                        },
                    )
                ],
            ),
        ],
        tools=[galaxy_tool],
    )
    # Get the model summary response
    summary = response.candidates[0].content.parts[0].text

    return summary, response

PROJECT_ID = "tpcg-datacollector"
REGION = "asia-northeast3"

summary, response = generate_function_call(
    #prompt="갤럭시 S24 카메라 정보를 가르쳐줘",
    #prompt="갤럭시 S24 카메라 정보를 설명해줘",
    #prompt="SM-S926NZVEKOO 카메라 정보를 설명해줘",
    #prompt="갤럭시 S24 정보를 가르쳐줘",
    #prompt="갤 S24 정보를 가르쳐줘",
    #prompt="갤S24 정보를 가르쳐줘",
    #prompt="갤럭시 S24 카메라 정보를 비교해 줘", 
    #prompt="갤럭시 S24과 S23 카메라 스펙을 비교해 줘",
    prompt="갤 S24과 S23 카메라 스펙을 비교해 줘",
    #prompt="갤럭시 SM-S711NZPWKOO과 SM-S926NZVEKOO 카메라 스펙을 비교해 줘",
    #prompt="갤럭시 SM-S711NZPWKOO과 SM-S926NZVEKOO의 특장점을 비교해 줘",
    project_id=PROJECT_ID, 
    location=REGION
)
print(summary)
#print(response)

"""
        response_json = {
            "모델": "갤럭시 S24 Ultra 자급제",
            "모델번호": "SM-S928NZTNKOO",
            "디스플레이": {
                "크기 (Main Display)": "172.5 mm",
                "해상도 (Main)": "3120 x 1440 (Quad HD+)",
                "종류 (Main)": "Dynamic AMOLED 2X",
                "색심도 (Main)": "16 M",
                "최대 주사율 (Main)": "120 Hz"
            },
            "프로세서": {
                 "CPU 속도": "3.39 GHz,3.1 GHz,2.9 GHz,2.2 GHz",
                 "CPU 종류": "Octa-Core"
            },
            "S펜 지원": "예",
            "카메라": {
                 "후면 카메라 - 화소 (Multiple)": "200.0 MP + 50.0 MP + 12.0 MP + 10.0 MP",
                 "후면 카메라 - 조리개 값 (Multiple)": "F1.7 , F3.4 , F2.2 , F2.4",
                 "후면 카메라 - 오토 포커스": "예",
                 "후면 카메라 - OIS": "예",
                 "후면 카메라 - 줌": "3배 및 5배 광학 줌, 광학 줌 수준의 2배 및 10배 줌(적응형 픽셀 센서 활용), 최대 100배 디지털 줌",
                 "전면 카메라 - 화소": "12.0 MP",
                 "전면 카메라 - 조리개 값": "F2.2", 
                 "전면 카메라 - 오토 포커스": "예",
                 "후면 카메라 - 플래쉬": "예", 
                 "후면 카메라 - Laser AF 센서": "예",
                 "동영상 녹화 해상도": "UHD 8K (7680 x 4320) @30fps",
                 "슬로우 모션": "240fps @FHD,120fps @UHD"
            },
            "메모리/스토리지(저장 용량)": {
                 "메모리 (GB)": "12 GB",
                 "스토리지(저장 용량) (TB)": "1 TB",
                 "사용 가능한 스토리지(저장 용량) (GB)": "996.5 GB"
            },
            "네트워크": {
                 "SIM 개수": "Dual-SIM",
                 "SIM 슬롯 타입": "SIM 1 + eSIM / Dual eSIM"
            },
            "네트워크 (S/W 사용)": {
                 "2G GSM": "GSM850,GSM900,DCS1800,PCS1900",
                 "3G UMTS": "B1(2100),B2(1900),B4(AWS),B5(850),B8(900)",
                 "4G FDD LTE": "B1(2100),B2(1900),B3(1800),B4(AWS),B5(850),B7(2600),B8(900),B12(700),B13(700),B17(700),B18(800),B19(800),B20(800),B25(1900),B26(850),B28(700),B66(AWS-3)",
                 "4G TDD LTE": "B38(2600),B39(1900),B40(2300),B41(2500)",
                 "5G FDD Sub6": "N1(2100),N2(1900),N3(1800),N5(850),N7(2600),N8(900),N12(700),N20(800),N25(1900),N26(850),N28(700),N66(AWS-3)",
                 "5G TDD Sub6": "N38(2600),N40(2300),N41(2500),N77(3700),N78(3500)"
            },
            "연결": {
                 "USB 인터페이스": "USB Type-C",
                 "USB 버전": "USB 3.2 Gen 1",
                 "위치 기술": "GPS,Glonass,Beidou,Galileo,QZSS",
                 "이어잭": "USB Type-C",
                 "MHL": "아니오",
                 "Wi-Fi": "802.11a/b/g/n/ac/ax 2.4GHz+5GHz+6GHz, HE160, MIMO, 1024-QAM",
                 "Wi-Fi Direct": "예",
                 "블루투스 버전": "Bluetooth v5.3",
                 "NFC": "예",
                 "UWB (Ultra-Wideband)": "예",
                 "PC 싱크": "Smart Switch (PC version)"
            },
            "운영체제": "Android",
            "기본 사양": {
                 "색상": "티타늄 그레이",
                 "형태": "터치 바"
            },
            "센서": "가속도 센서,기압 센서,지문 센서,자이로 센서,지자기 센서,홀 센서,조도 센서,근접 센서",
            "외관 사양": {
                 "크기(세로x가로x두께, mm)": "162.3 x 79.0 x 8.6",
                 "무게(g)": "232"
            },
            "배터리": {
                 "인터넷 사용 시간(LTE) (Hours)": "최대 27",
                 "인터넷 사용 시간(Wi-Fi) (Hours)": "최대 28",
                 "비디오 재생 시간 (Hours, Wireless)": "최대 30",
                 "배터리 용량(mAh, Typical)": "5000",
                 "교체 가능": "아니오",
                 "오디오 재생 시간 (Hours, Wireless)": "최대 95"
            },
            "오디오/비디오": {
                 "스테레오 지원": "예",
                 "동영상 지원 포맷": "MP4,M4V,3GP,3G2,AVI,FLV,MKV,WEBM",
                 "동영상 지원 해상도": "UHD 8K (7680 x 4320) @60fps",
                 "오디오 지원 포맷": "MP3,M4A,3GA,AAC,OGG,OGA,WAV,AMR,AWB,FLAC,MID,MIDI,XMF,MXMF,IMY,RTTTL,RTX,OTA,DFF,DSF,APE"
            },
            "서비스": {
                 "Gear 서포트": "갤럭시 버즈2 프로,갤럭시 버즈 프로,갤럭시 버즈 라이브,갤럭시 버즈+,갤럭시 버즈2,갤럭시 버즈,갤럭시 버즈 FE,갤럭시 핏2,갤럭시 핏e,갤럭시 핏,갤럭시 워치6,갤럭시 워치5,갤럭시 워치4,갤럭시 워치3,갤럭시 워치,갤럭시 워치 액티브2,갤럭시 워치 액티브",
                 "삼성 덱스 서포트": "지원",
                 "모바일 TV": "아니오",
                 "블루투스 보청기 지원": "보청기용 안드로이드 오디오 스트리밍(ASHA)",
                 "SmartThings 지원": "지원"
            },
            "상품 기본정보": {
                 "제품명": "5G NR 이동통신용 무선설비의 기기(3.5 GHz)(육상이동국의 송수신장치)",
                 "제조자/수입자": "삼성전자㈜",
                 "제조국가": "한국, 베트남",
                 "KC 인증 필 유무": "KC 인증 로고R-C-SEC-SMS928",
                 "동일모델의 출시년월": "24년 1월",
                 "A/S 책임자와 전화번호": "삼성전자서비스센터/1588-3366",
                 "품질보증기준": "결함·하자 등에 따른 소비자 피해에 대해서는 소비자분쟁해결기준(소비자기본법 제16조)에 따라 보상 가능"
            }
        }
        api_response = json.dumps(response_json)
"""
