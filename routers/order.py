from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

import json
import routers.dummy as dummy

router = APIRouter(
  prefix="/order",
  tags=['apis'],
  responses={404: {"description": "Not found"}}
)

@router.post("/")
async def order(request: Request):
    """
    https://medium.com/google-cloud/building-of-python-webhook-to-integrate-the-cloudsql-database-with-chatbot-in-dialogflow-cx-e6a07c45f6fe
    """
    print('request', request)
    data = await request.json()
    print('data', data)

    tag = data.get("fulfillmentInfo")["tag"]
    session_info = data.get("sessionInfo")
    
    print("parameters", session_info["parameters"])
    color = session_info["parameters"]["color"]
    size = session_info["parameters"]["size"]
    print("color", color, ",", "size", size)

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

    message = "Hell World"
    message = "Test Fulfillment Webhook / Cloud Run / FastAPI"
    response = {"fulfillment_response": {"messages": [{"text": {"text": [message]}}]}}
    #return {"message": "Hell World"}
    return response