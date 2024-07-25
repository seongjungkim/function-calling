from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

import json
import re

import vertexai
from langchain_google_vertexai import VertexAI

from langchain_community.retrievers import (
    GoogleVertexAIMultiTurnSearchRetriever,
    GoogleVertexAISearchRetriever,
)

import routers.dummy as dummy

from utils import bigqueryapi, postgresqlapi

router = APIRouter(
  prefix="/solution",
  tags=['apis'],
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

    """
    From Dialogflow CX
    {
        'detectIntentResponseId': '1b7a14c4-3508-4afe-a256-4973d3ee4438', 
        'intentInfo': {
            'lastMatchedIntent': 'projects/samsung-poc-425503/locations/global/agents/7f1a678c-14c5-432e-8912-963357595441/intents/0adebb70-a727-4687-b8bc-fbbc2ac0b665', 
            'parameters': {
                'size': {'originalValue': 'large', 'resolvedValue': 'large'}, 
                'color': {'originalValue': 'yellow', 'resolvedValue': 'yellow'}
            }, 
            'displayName': 'order.new', 
            'confidence': 0.75953496
        }, 
        'pageInfo': {
            'currentPage': 'projects/samsung-poc-425503/locations/global/agents/7f1a678c-14c5-432e-8912-963357595441/flows/00000000-0000-0000-0000-000000000000/pages/ce0b88c4-9292-455c-9c59-ec153dad94cc', 
            'displayName': 'New Order'
        }, 
        'sessionInfo': {
            'session': 'projects/samsung-poc-425503/locations/global/agents/7f1a678c-14c5-432e-8912-963357595441/sessions/48fe0a-4e4-941-b55-b7a2e367a', 
            'parameters': {'color': 'yellow', 'size': 'large'}
        }, '
        fulfillmentInfo': {'tag': 'check order option'}, 
        'messages': [
            {
                'text': {
                    'text': ["Ok, let's start a new order."], 
                    'redactedText': ["Ok, let's start a new order."]
                }, 
                'responseType': 'ENTRY_PROMPT', 
                'source': 'VIRTUAL_AGENT'
            }
        ], 
        'text': 'I need a large, yellow shirt', 
        'languageCode': 'en', 
        'languageInfo': {
            'inputLanguageCode': 'en', 
            'resolvedLanguageCode': 'en', 
            'confidenceScore': 1.0
        }
    }
    """

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
        #print(doc)
        #print('page_content', doc.page_content)
        print('metadata', doc.metadata)
        sources.append(doc.metadata.get('source'))
    print('sources', sources)

    message = "Hell World"
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


@router.post("/get_release_date")
async def get_release_date(request: Request):
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
    product = session_info["parameters"].get("product-temp")
    print("product", product, ",", "attribute", attribute)

    result = invoke(query)
    print('result', result, type(result))
    #result = None
    #if type(results) is dict:
    #    result = results
    #elif type(results) is list:
    #    result = results[0]
    
    companies = result.get("companies")
    models = result["models"]
    release_date_yesno = result["release_date_yesno"]
    samsung_product_yesno = result["samsung_product_yesno"]
    notsamsung_product_yesno = result["notsamsung_product_yesno"]
    required_feature = result["required_feature"]
    sensitive_words_yesno = result["sensitive_words_yesno"]
    print(companies, models, release_date_yesno, samsung_product_yesno, 
        notsamsung_product_yesno, required_feature, sensitive_words_yesno)

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

    query = f"""SELECT
        DISTINCT "펫네임", "출시일"
    FROM
        "Sample_s23"
    WHERE
        "펫네임" SIMILAR TO '%{'%|%'.join(models)}%'
    UNION
    SELECT
        DISTINCT "펫네임", "출시일"
    FROM
        "Sample_s24"
    WHERE
        "펫네임" SIMILAR TO '%{'%|%'.join(models)}%'
    ORDER BY "펫네임"
    """
    print('query', query)
    rows = postgresql_api.query_all(query)
    print(rows)

    message = "Hell World"
    message = "Fulfillment Webhook / Cloud Run / FastAPI"
    release_dates = []
    for row in rows:
        model, release_date = row
        dict = {"model": model, "release_date": release_date}
        release_dates.append(dict)

    fulfillment_response = {
        "fulfillment_response": {
            "messages": [{"text": {"text": [message]}}]
        },
        "session_info": session_info,
        #"page_info": {"current_page": "1"}, 
        "payload": { "models": release_dates }
    }
    print('fulfillment_response', fulfillment_response)
    #return {"message": "Hell World"}
    return fulfillment_response

def invoke(question):
    from mdextractor import extract_md_blocks

    #https://ai.google.dev/gemini-api/docs/json-mode?hl=ko&lang=python

    PROJECT_ID = "samsung-poc-425503"
    #LOCATION = "us-central1"
    LOCATION = "global"
    REGION = "asia-northeast3"
    AGENT_ID = "f0cd1f27-d3e9-427c-9f59-fc7bac7a7b1c"

    prompt = f"""
    당신은 제품 정보를 분석하는 전문 AI입니다.
    문에서 회사 목록, 제품 모델 목록, 제품 모델별로 출시일의 질문여부, 
    답변으로 요구하는 특성이 무엇인지, 삼성전자 제품인지, 삼성전자 이외 제품 포함여부, 민감단어 포함여부, 분류해주세요. 
    삼성전자 제품이면 대표 모델명으로 변경해 주세요. 예제: ["갤럭시 S24", "S24", "갤럭시 24",  "갤24"] -> "갤럭시 S24"
    
    답변을 다음 key를 가진 JSON 형식으로 만들어주세요.

    Key: "question", "companies", "models", "release_date_yesno", "samsung_product_yesno", "notsamsung_product_yesno", "required_feature", "sensitive_words_yesno"

    질문: 
    {question}
    """

    #model_name = "gemini-1.5-pro-001"
    model_name = "gemini-1.5-flash-001"
    vertexai.init(project=PROJECT_ID, location=REGION)
    llm = VertexAI(model_name=model_name, max_output_tokens=1000)
    response_text = llm.invoke(
        prompt 
    ).replace("*", "")
    print('response_text', response_text)

    blocks = extract_md_blocks(response_text)
    print('response_text', blocks[0], type(blocks[0]))
    json_obj = json.loads(blocks[0])
    print('json_obj', json_obj, type(json_obj))
    return json_obj