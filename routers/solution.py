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
import utils.common as common

from utils import bigqueryapi, postgresqlapi

router = APIRouter(
  prefix="/solution",
  tags=['apis'],
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

@router.post("/")
async def solution(request: Request):
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
    
    print("parameters", session_info["parameters"])
    attribute = session_info["parameters"].get("attribute")
    product = session_info["parameters"].get("product")
    print("product", product, ",", "attribute", attribute)

    retriever = GoogleVertexAISearchRetriever(
        project_id=PROJECT_ID,
        location_id=SEARCH_LOCATION_ID,
        data_store_id=DATA_STORE_ID,
        max_documents=3,
    )

    result = retriever.invoke(question)
    sources = []
    for doc in result:
        print(doc, type(doc))
        #print('page_content', doc.page_content)
        print('metadata', doc.metadata, type(doc.metadata))
        sources.append(doc.metadata.get('source'))
    print('sources', sources)

    message = "Fulfillment Webhook / Cloud Run / FastAPI"
    fulfillment_response = common.make_response(message, session_info,
                                    intent_name, decision_intent_name,
                                    sources=sources)
    return fulfillment_response


@router.post("/get_release_date")
async def get_release_date(request: Request):
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
    
    print("parameters", session_info["parameters"])
    attribute = session_info["parameters"].get("attribute")
    product = session_info["parameters"].get("product-temp")
    print("product", product, ",", "attribute", attribute)

    result = check_release_date(question)
    print('result', result, type(result))
    
    companies = result.get("companies")
    models = result["models"]
    samsung_models = result["samsung_models"]
    othercompany_models = result["othercompany_models"]

    """
    release_date_yesno = result["release_date_yesno"]
    samsung_product_yesno = result["samsung_product_yesno"]
    othercompany_product_yesno = result["othercompany_product_yesno"]
    sensitive_words_yesno = result["sensitive_words_yesno"]
    """
    release_date_yesno = common.get_bool(result.get("release_date_yesno", False))
    samsung_product_yesno = common.get_bool(result.get("samsung_product_yesno", False))
    other_product_yesno = common.get_bool(result.get("othercompany_product_yesno", False))
    sensitive_words_yesno = common.get_bool(result.get("sensitive_words_yesno", False))
    required_feature = result["required_feature"]

    print(companies, models, samsung_models, othercompany_models, release_date_yesno, release_date_yesno, 
        samsung_product_yesno, other_product_yesno, required_feature, sensitive_words_yesno)
    
    if other_product_yesno == True or sensitive_words_yesno == True:
        decision_intent_name = "avoidance.phrase"
        message = common.generate_avoidance(question)

        print("othercompany_product_yesno", other_product_yesno, type(other_product_yesno))
        fulfillment_response = common.make_response(message, session_info, 
                                        intent_name, decision_intent_name)
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response
    elif release_date_yesno == False:
        decision_intent_name = "others"
        message = "Mismatching Intent"

        fulfillment_response = common.make_response(message, session_info, 
                                        intent_name, decision_intent_name)
        print("fulfillment_response", fulfillment_response)
        return fulfillment_response

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

    message = "Fulfillment Webhook / Cloud Run / FastAPI"
    release_dates = []
    for row in rows:
        model, release_date = row
        dict = {"model": model, "release_date": release_date}
        release_dates.append(dict)

    if other_product_yesno and \
        len(othercompany_models) > 0:
        common.generate_avoidance(' '.join(othercompany_models))

    fulfillment_response = common.make_response(message, session_info,
                                    intent_name, decision_intent_name,
                                    sources=release_dates, models=release_dates)
    print('fulfillment_response', fulfillment_response)
    return fulfillment_response

def check_release_date(question):
    from mdextractor import extract_md_blocks

    #https://ai.google.dev/gemini-api/docs/json-mode?hl=ko&lang=python

    prompt = prompts.release_date_prompt + f"""{question}"""

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
