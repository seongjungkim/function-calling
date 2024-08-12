from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

import json
import re
import os

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
import utils.common as common

from utils import bigqueryapi, postgresqlapi

router = APIRouter(
  prefix="/product",
  tags=['product'],
  responses={404: {"description": "Not found"}}
)

PROJECT_ID = "samsung-poc-425503"
#REGION = "asia-northeast3"
REGION = "us-central1"

#model_name = "gemini-1.5-pro-001"
model_name = "gemini-1.5-flash-001"

SEARCH_LOCATION_ID = "global"  # Set to your data store location
SEARCH_ENGINE_ID = "samsungsvc-html_1721012292828"  # Set to your search app ID
DATA_STORE_ID = "samsungsvc-html_1721012095245"  # Set to your data store ID
#AGENT_ID = "f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c"

# AlloyDB 연동
ALLOY_IP="10.40.160.2"
ALLOY_USER="postgres"
ALLOY_PASS="tpcg1234"
ALLOY_PORT="5432"
ALLOY_NAME="postgres"

@router.post("/description")
async def product(request: Request):
    print('request', request)
    data = await request.json()
    print('data', data)

    intent_info = data.get("intentInfo")
    intent_name = intent_info.get("displayName") if intent_info else None
    decision_intent_name = intent_name

    tag = data.get("fulfillmentInfo")["tag"]
    question = data.get("text")
    print("question", question)
    session_info = data.get("sessionInfo")

    base_prompt = prompts.product_description_prompt
    result = check_prompt(base_prompt, question)
    print('result', result, type(result))
    
    products = result.get("products", [])
    models = result.get("models", [])
    series = result.get("series", [])

    comparison_yesno = common.get_bool(result.get("comparison_yesno", False))
    description_yesno = common.get_bool(result.get("description_yesno", False))
    samsung_product_yesno = common.get_bool(result.get("samsung_product_yesno", False))
    other_product_yesno = common.get_bool(result.get("competitors_product_yesno", False))

    features = result.get("features", [])
    features = [features] if isinstance(features, str) else features
    features = [x for x in features if x not in ["기능"]]
    method = result.get("method", [])
    print(products, models, series, comparison_yesno, description_yesno, 
        samsung_product_yesno, other_product_yesno, features)

    print("other_product_yesno", other_product_yesno, type(other_product_yesno))
    if other_product_yesno == True:
        # 타사제품이 포함되어 있는 경우
        decision_intent_name = "avoidance.phrase"
        message = common.generate_avoidance(question)

        print("other_product_yesno", other_product_yesno, type(other_product_yesno))
        fulfillment_response = common.make_response(message, session_info, 
                                        intent_name, decision_intent_name)
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response
    elif comparison_yesno == True and description_yesno == False:
        # 설명이 아니지만 비교 하는 경우
        decision_intent_name = "product.comparison"
        message = "Mismatching Intent"

        columns, rows, data = query_spec(products, models, features)
        if len(columns) == 0 or data == None:
            fulfillment_response = generate_others(intent_name, session_info)
            print("fulfillment_response", fulfillment_response)
            return fulfillment_response
        
        message = generate_product(question, columns, data)

        fulfillment_response = common.make_response(message, session_info, 
                                        intent_name, decision_intent_name,
                                        columns=columns, rows=rows)
        
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response
    elif (len(products) == 0 and len(models) == 0) or \
        len(features) == 0:
        fulfillment_response = generate_others(intent_name, session_info)

        print('products', products)
        print('models', models)
        print('features', features)
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response
    
    columns, rows, data = query_spec(products, models, features)
    if len(columns) == 0 or data == None:
        fulfillment_response = generate_others(intent_name, session_info)
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response

    message = "Fulfillment Webhook / Product Description"
    message = generate_product(question, columns, data)

    fulfillment_response = common.make_response(message, session_info, 
                                    intent_name, decision_intent_name,
                                    columns=columns, rows=rows)
    print('fulfillment_response', fulfillment_response)
    
    return fulfillment_response


@router.post("/comparison")
async def compare_products(request: Request):
    """
    https://medium.com/google-cloud/building-of-python-webhook-to-integrate-the-cloudsql-database-with-chatbot-in-dialogflow-cx-e6a07c45f6fe
    """
    print('request', request)
    data = await request.json()
    print('data', data)

    intent_info = data.get("intentInfo")
    intent_name = intent_info.get("displayName") if intent_info else None
    decision_intent_name = intent_name

    tag = data.get("fulfillmentInfo")["tag"]
    question = data.get("text")
    print("question", question)
    session_info = data.get("sessionInfo")
    
    base_prompt = prompts.product_comparison_prompt
    result = check_prompt(base_prompt, question)
    print('result', result, type(result))
    
    products = result.get("products", [])
    models = result.get("models", [])
    series = result.get("series", [])
    """
    comparison_yesno = result.get("comparison_yesno", False)
    description_yesno = result.get("description_yesno", False)
    samsung_product_yesno = result.get("samsung_product_yesno", False)
    other_product_yesno = result.get("competitors_product_yesno", False)
    """
    comparison_yesno = common.get_bool(result.get("comparison_yesno", False))
    description_yesno = common.get_bool(result.get("description_yesno", False))
    samsung_product_yesno = common.get_bool(result.get("samsung_product_yesno", False))
    other_product_yesno = common.get_bool(result.get("competitors_product_yesno", False))

    features = result.get("features", [])
    method = result.get("method", [])
    print(products, models, series, comparison_yesno, description_yesno, 
        samsung_product_yesno, other_product_yesno, features)

    print("competitors_product_yesno", other_product_yesno, type(other_product_yesno))
    if other_product_yesno == True:
        # 타사제품이 포함되어 있는 경우
        decision_intent_name = "avoidance.phrase"
        message = common.generate_avoidance(question)

        print("competitors_product_yesno", other_product_yesno, type(other_product_yesno))
        fulfillment_response = common.make_response(message, session_info, 
                                        intent_name, decision_intent_name)
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response
    elif comparison_yesno == False and description_yesno == True:
        # 비교는 아니지만 설명을 하는 경우
        decision_intent_name = "galaxy.query"
        message = "Mismatching Intent"

        columns, rows, data = query_spec(products, models, features)
        if len(columns) == 0 or data == None:
            fulfillment_response = generate_others(intent_name, session_info)
            print("fulfillment_response", fulfillment_response)
            return fulfillment_response
        
        message = generate_product(question, columns, data)

        fulfillment_response = common.make_response(message, session_info, 
                                        intent_name, decision_intent_name,
                                        columns=columns, rows=rows)
        
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response
    elif comparison_yesno == False or \
        (len(products) == 0 and len(models) == 0):
        fulfillment_response = generate_others(intent_name, session_info)
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response

    columns, rows, data = query_spec(products, models, features)
    if len(columns) == 0 or data == None:
        fulfillment_response = generate_others(intent_name, session_info)
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response

    message = "Fulfillment Webhook / Product Comparison"
    message = generate_product(question, columns, data)

    fulfillment_response = common.make_response(message, session_info, 
                                    intent_name, decision_intent_name,
                                    columns=columns, rows=rows)
    print('fulfillment_response', fulfillment_response)
    return fulfillment_response

def check_prompt(base_prompt, question):
    from mdextractor import extract_md_blocks

    #https://ai.google.dev/gemini-api/docs/json-mode?hl=ko&lang=python

    prompt = base_prompt + f"""
    {question}"""
    print('prompt', prompt)

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

def check_columns(all_columns, features):
    columns = []
    if isinstance(features, str):
        if features == "외관" or features == "무게":
            columns.append("기본")
            columns.append("외관")
            return columns
        
        if features in all_columns:
            columns.append(features)
        else:
            print('key', features, 'similarity')
            feature = common.find_similarity_feature(features, all_columns)
            if feature:
                columns.append(feature)
    elif isinstance(features, list) and len(features) == 0:
        for key in all_columns.keys():
            #전체에서 제외되는 항목 (비교대상이 너무 많아서)
            if key in ["운영체제", "기본", "네트워크", "서비스", "센서", "연결", "오디오/비디오"]:
                continue

            if key in all_columns:
                columns.append(key)
            else:
                print('key', key, 'similarity')
                feature = common.find_similarity_feature(key, all_columns)
                if feature:
                    columns.append(feature)
    elif isinstance(features, list):
        for key in features:
            if key == "외관" or key == "무게":
                columns.append("기본")
                columns.append("외관")
                continue

            if key in all_columns:
                columns.append(key)
            else:
                print('key', key, 'similarity')
                feature = common.find_similarity_feature(key, all_columns)
                if feature:
                    columns.append(feature)
    
    return columns


def query_spec(products, models, features):
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

    postgresql_api = postgresqlapi.PostgresqlAPI(
        host=ALLOY_IP, 
        port=ALLOY_PORT, 
        user=ALLOY_USER, 
        password=ALLOY_PASS, 
        dbname=ALLOY_NAME)
    
    keys = check_columns(all_columns, features)
    print('keys', keys, type(keys))
    if len(keys) == 0:
        return keys, None, None
    
    columns = []
    for key in keys:
        columns = columns + all_columns[key]

    #columns.append("시리즈")
    columns.insert(0, "시리즈")
    if len(models) > 0: 
        #columns.append("모델코드")
        columns.insert(1, "모델코드")
    
    print('columns', '","'.join(columns))
    print("products", '","'.join(products))
    print('models', '","'.join(models))

    #라인업,시리즈,상품명,모델코드
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

    data = []
    series_list = []
    for row in rows:
        #print(row)
        series = row[0]
        cnt = sum(series in s for s in data)
        if len(columns) > 20 and cnt >= 2: continue
        data.append(','.join(row))

    return columns, rows, data

def generate_others(intent_name, session_info):
    # 비교가 아니거나 비교제품 또는 모델이 없는 경우
    decision_intent_name = "others"
    message = "Mismatching Intent"

    fulfillment_response = common.make_response(message, session_info, 
                                        intent_name, decision_intent_name)
    print("fulfillment_response", fulfillment_response)
    return fulfillment_response

def generate_product(question, columns, data):
    #https://ai.google.dev/api/generate-content?hl=ko#text
    prompt = prompts.product_generation_prompt
    prompt = prompt.replace("##QUESTION##", question)
    prompt = prompt.replace("##COLUMNS##", ",".join(columns))
    prompt = prompt.replace("##DATA##", "\n".join(data))
    print("Generation Prompt", prompt)

    vertexai.init(project=PROJECT_ID, location=REGION)

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
