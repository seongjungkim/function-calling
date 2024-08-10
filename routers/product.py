from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

import json
import re

import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models

from langchain_google_vertexai import VertexAI
from langchain_community.retrievers import (
    GoogleVertexAIMultiTurnSearchRetriever,
    GoogleVertexAISearchRetriever,
)

import routers.dummy as dummy
import routers.prompts as prompts
import routers.avoidance as avoidance

from utils import bigqueryapi, postgresqlapi

router = APIRouter(
  prefix="/product",
  tags=['product'],
  responses={404: {"description": "Not found"}}
)

@router.post("/")
async def solution(request: Request):
    """
    https://medium.com/google-cloud/building-of-python-webhook-to-integrate-the-cloudsql-database-with-chatbot-in-dialogflow-cx-e6a07c45f6fe
    """
    print('request', request)
    data = await request.json()
    print('data', data)

    tag = data.get("fulfillmentInfo")["tag"]
    query = data.get("text")
    print("query", query)
    session_info = data.get("sessionInfo")
    
    print("parameters", session_info["parameters"])
    attribute = session_info["parameters"].get("attribute")
    product = session_info["parameters"].get("product")
    print("product", product, ",", "attribute", attribute)

    PROJECT_ID = "samsung-poc-425503"  # Set to your Project ID
    LOCATION_ID = "global"  # Set to your data store location
    SEARCH_ENGINE_ID = "samsungsvc-html_1721012292828"  # Set to your search app ID
    DATA_STORE_ID = "samsungsvc-html_1721012095245"  # Set to your data store ID

    retriever = GoogleVertexAISearchRetriever(
        project_id=PROJECT_ID,
        location_id=LOCATION_ID,
        data_store_id=DATA_STORE_ID,
        max_documents=3,
    )

    result = retriever.invoke(query)
    sources = []
    for doc in result:
        print(doc, type(doc))
        #print('page_content', doc.page_content)
        print('metadata', doc.metadata, type(doc.metadata))
        sources.append(doc.metadata.get('source'))
    print('sources', sources)

    message = "Fulfillment Webhook / Cloud Run / FastAPI"
    fulfillment_response = {
        "fulfillment_response": {
            "messages": [{"text": {"text": [message]}}]
        },
        "session_info": session_info,
        "page_info": {"current_page": "1"}, 
        "payload": { "display": "payload test", "sources": sources }
    }
    #return {"message": "Hell World"}
    return fulfillment_response


@router.post("/comparison")
async def compare_products(request: Request):
    """
    https://medium.com/google-cloud/building-of-python-webhook-to-integrate-the-cloudsql-database-with-chatbot-in-dialogflow-cx-e6a07c45f6fe
    """
    print('request', request)
    data = await request.json()
    print('data', data)

    tag = data.get("fulfillmentInfo")["tag"]
    question = data.get("text")
    print("question", question)
    session_info = data.get("sessionInfo")
    
    print("parameters", session_info["parameters"])
    attribute = session_info["parameters"].get("attribute")
    product = session_info["parameters"].get("product-temp")
    print("product", product, ",", "attribute", attribute)

    result = check_comparison(question)
    print('result', result, type(result))
    
    products = result.get("products", [])
    models = result.get("models", [])
    series = result.get("series", [])
    comparison_yesno = result.get("comparison_yesno", False)
    description_yesno = result.get("description_yesno", False)
    samsung_product_yesno = result.get("samsung_product_yesno", False)
    other_product_yesno = result.get("othercompany_product_yesno", False)
    feature = result.get("feature", [])
    method = result.get("method", [])
    print(products, models, series, comparison_yesno, description_yesno, 
        samsung_product_yesno, other_product_yesno, feature)

    print("othercompany_product_yesno", other_product_yesno, type(other_product_yesno))
    if other_product_yesno == "yes" or \
        (isinstance(other_product_yesno, bool) and other_product_yesno):
        avoidance_result = avoidance.generate_avoidance(question)
        print("othercompany_product_yesno", other_product_yesno, type(other_product_yesno))
        fulfillment_response = {
            "fulfillment_response": {
                "messages": [{"text": {"text": f"{avoidance_result}"}}]
            },
            "session_info": session_info,
            "payload": { "decision_intent": "avoidance.phrase" }
        }
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response

    all_columns = {
    "S펜": ["S펜 지원"],
    "센서": ["센서"],
    "운영체제": ["운영체제"],
    "디스플레이": ["디스플레이_크기 (Main Display)", "디스플레이_해상도 (Main)", "디스플레이_종류 (Main)", "디스플레이_색심도 (Main)",
        "디스플레이_크기 (Sub)", "디스플레이_해상도 (Sub)", "디스플레이_종류 (Sub)", "디스플레이_색심도 (Sub)", "디스플레이_최대 주사율 (Main)"],
    "프로세서": ["프로세서_CPU 속도", "프로세서_CPU 종류", "프로세서_CPU"],
    "카메라": ["카메라_후면 카메라 - 화소 (Multiple)", "카메라_후면 카메라 - 조리개 값 (Multiple)", "카메라_후면 카메라 - 오토 포커스", 
        "카메라_후면 카메라 - OIS", "카메라_후면 카메라 - 줌", "카메라_후면 카메라 - Laser AF 센서", "카메라_후면 카메라 - 플래쉬", 
        "카메라_전면 카메라 - 조리개 값", "카메라_전면 카메라 - 오토 포커스", "카메라_전면 카메라 - OIS",
        "카메라_전면 카메라 - 플래쉬", "카메라_동영상 녹화 해상도",
        "카메라_커버 카메라 - 화소", "카메라_커버 카메라 - 조리개 값", "카메라_커버 카메라 - 오토 포커스", 
        "카메라_언더 디스플레이 카메라 - 화소", "카메라_언더 디스플레이 카메라 - 조리개 값", "카메라_언더 디스플레이 카메라 - 오토 포커스", 
        "카메라_언더 디스플레이 카메라 - OIS",
        "카메라_슬로우 모션"], #, "카메라_후면 카메라 줌"
    "메모리/스토리지": ["메모리/스토리지(저장 용량)_메모리 (GB)", "메모리/스토리지(저장 용량)_스토리지(저장 용", 
        "메모리/스토리지(저장 용량)_사용 가능한 스토", "메모리/스토리지(저장 용량)_외장 스토리지(저"],
    "네트워크": ["네트워크_SIM 개수", "네트워크_SIM 사이즈", "네트워크_SIM 슬롯 타입", "네트워크 (S/W 사용)_2G GSM",
        "네트워크 (S/W 사용)_3G UMTS", "네트워크 (S/W 사용)_4G FDD LTE", "네트워크 (S/W 사용)_4G TDD LTE",
        "네트워크 (S/W 사용)_5G TDD Sub6", "네트워크 (S/W 사용)_5G FDD Sub6", "네트워크_인프라"],
    "연결": ["연결_USB 인터페이스", "연결_USB 버전", "연결_위치 기술", "연결_이어잭", "연결_MHL", "연결_Wi-Fi", 
        "연결_Wi-Fi Direct", "연결_블루투스 버전", "연결_NFC", "연결_PC 싱크", "연결_UWB (Ultra-Wideband)"],
    "기본": ["기본 사양_색상", "기본 사양_형태"],
    "외관": ["외관 사양_크기(세로x가로x두께, mm)", "외관 사양_무게(g)", "외관 사양_접힌 상태시 크기(세로x가로x두께, mm)"],
    "배터리": ["배터리_인터넷 사용 시간(LTE) (Hours)", "배터리_인터넷 사용 시간(Wi-Fi) (Hours)", "배터리_비디오 재생 시간 (Hours)", 
        "배터리_오디오 재생 시간 (Hours)", "배터리_연속 통화시간(4G LTE) (Hours)",
        "배터리_비디오 재생 시간 (Hours, Wireless)", "배터리_오디오 재생 시간 (Hours, Wireless)"], #"배터리_배터리 용량(mAh, Typical)", "배터리_교체 가능", 
    "오디오/비디오": ["오디오/비디오_스테레오 지원", "오디오/비디오_동영상 지원 포맷", "오디오/비디오_동영상 지원 해상도", "오디오/비디오_오디오 지원 포맷"],
    "서비스": ["서비스_Gear 서포트", "서비스_삼성 덱스 서포트", "서비스_모바일 TV", "서비스_블루투스 보청기 지원", "서비스_SmartThings 지원"],
    }

    columns = ["카메라_후면 카메라 - 화소 (Multiple)", "카메라_후면 카메라 - 조리개 값 (Multiple)", "카메라_후면 카메라 - 오토 포커스", 
        "카메라_후면 카메라 - OIS", "카메라_후면 카메라 줌", "카메라_후면 카메라 - 줌", "카메라_후면 카메라 - Laser AF 센서", 
        "카메라_전면 카메라 - 조리개 값", "카메라_전면 카메라 - 오토 포커스",
        "카메라_전면 카메라 - OIS", "카메라_후면 카메라 - 플래쉬", "카메라_전면 카메라 - 플래쉬", "카메라_동영상 녹화 해상도",
        "카메라_커버 카메라 - 화소", "카메라_커버 카메라 - 조리개 값", "카메라_커버 카메라 - 오토 포커스", 
        "카메라_언더 디스플레이 카메라 - 화소", "카메라_언더 디스플레이 카메라 - 조리개 값", "카메라_언더 디스플레이 카메라 - 오토 포커스", 
        "카메라_언더 디스플레이 카메라 - OIS",
        "카메라_슬로우 모션"]

    # AlloyDB 연동
    """ """
    ALLOY_IP="10.40.160.2"
    ALLOY_USER="postgres"
    ALLOY_PASS="tpcg1234"
    ALLOY_PORT="5432"
    ALLOY_NAME="postgres"
    """ """
    postgresql_api = postgresqlapi.PostgresqlAPI(
        host=ALLOY_IP, 
        port=ALLOY_PORT, 
        user=ALLOY_USER, 
        password=ALLOY_PASS, 
        dbname=ALLOY_NAME)
    
    columns = []
    if len(feature) == 0:
        for key in all_columns.keys():
            #print(key)
            if key in ["운영체제", "기본", "네트워크", "서비스", "센서", "연결", "오디오/비디오"]:
                continue
            columns = columns + all_columns[key]
    elif isinstance(feature, str):
        try:
            columns = all_columns[feature]
        except KeyError as e:
            feature = find_similarity_feature(feature, all_columns)
            columns = all_columns[feature]
    elif isinstance(feature, list):
        for key in feature:
            try:
                columns = columns + all_columns[key]
            except KeyError as e:
                key = find_similarity_feature(key, all_columns)
                columns = columns + all_columns[key]

    columns.append("시리즈")
    if len(models) > 0: 
        columns.append("모델코드")
    print('columns', '","'.join(columns))
    print("products", '","'.join(products))
    print('models', '","'.join(models))
    #series = []
    #models = []
    """라인업,시리즈,상품명,모델코드"""
    query = f"""SELECT
    DISTINCT "{'","'.join(columns)}"
FROM
    pivot_spec_s23
WHERE
    {("--" if len(products) == 0 else "")}"시리즈" SIMILAR TO '%{'%|%'.join(products)}%'
    {("--" if len(models) == 0 else "")}"모델코드" IN ('{"','".join(models)}')
UNION
SELECT
    DISTINCT "{'","'.join(columns)}"
FROM
    pivot_spec_s24
WHERE
    {("--" if len(products) == 0 else "")}"시리즈" SIMILAR TO '%{'%|%'.join(products)}%'
    {("--" if len(models) == 0 else "")}"모델코드" IN ('{"','".join(models)}')
ORDER BY "시리즈"
"""
    print('query', query)
    rows = postgresql_api.query_all(query)
    #print(rows, type(rows))

    message = "Fulfillment Webhook / Product Comparison"
    data = []
    for row in rows:
        #print(row)
        #model, release_date = row
        #dict = {"model": model, "release_date": release_date}
        data.append(','.join(row))

    message = generate_comparison(question, columns, data)

    fulfillment_response = {
        "fulfillment_response": {
            "messages": [{"text": {"text": [message]}}]
        },
        "session_info": session_info,
        #"page_info": {"current_page": "1"}, 
        "payload": { "columns": columns, "rows": rows }
    }
    print('fulfillment_response', fulfillment_response)
    #return {"message": "Hell World"}
    return fulfillment_response

def check_comparison(question):
    from mdextractor import extract_md_blocks

    #https://ai.google.dev/gemini-api/docs/json-mode?hl=ko&lang=python

    PROJECT_ID = "samsung-poc-425503"
    #LOCATION = "us-central1"
    LOCATION = "global"
    REGION = "asia-northeast3"
    AGENT_ID = "f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c"

    prompt = prompts.comparison_prompt + f"""
    {question}"""
    print('prompt', prompt)

    #model_name = "gemini-1.5-pro-001"
    model_name = "gemini-1.5-flash-001"
    vertexai.init(project=PROJECT_ID, location=REGION)
    llm = VertexAI(model_name=model_name, max_output_tokens=1000)
    response_text = llm.invoke(
        prompt 
    )
    print('response_text', response_text)

    blocks = extract_md_blocks(response_text)
    print('response_text', blocks[0], type(blocks[0]))
    json_obj = json.loads(blocks[0])
    print('json_obj', json_obj, type(json_obj))
    return json_obj

def generate_comparison(question, columns, data):
    #https://ai.google.dev/api/generate-content?hl=ko#text
    prompt = prompts.comparison_generation_prompt
    prompt = prompt.replace("##QUESTION##", question)
    prompt = prompt.replace("##COLUMNS##", ",".join(columns))
    prompt = prompt.replace("##DATA##", "\n".join(data))
    print("Generation Prompt", prompt)

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

def word2vec(word):
    from collections import Counter
    from math import sqrt

    # count the characters in word
    cw = Counter(word)
    # precomputes a set of the different characters
    sw = set(cw)
    # precomputes the "length" of the word vector
    lw = sqrt(sum(c*c for c in cw.values()))

    # return a tuple
    return cw, sw, lw

def cosdis(v1, v2):
    # which characters are common to the two words?
    common = v1[1].intersection(v2[1])
    # by definition of cosine distance we have
    return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]

def find_similarity_feature(feature, columns):
    va = word2vec(feature)

    similarity_feature = None
    max_sim = 0
    for key in columns.keys():
        vb = word2vec(key)
        sim = cosdis(va,vb)
        print("key", key, sim)
        max_sim, similarity_feature = (sim, key) if sim > max_sim \
            else (max_sim, similarity_feature)

    return similarity_feature