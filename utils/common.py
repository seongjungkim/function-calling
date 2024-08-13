from string import ( punctuation, whitespace, digits, ascii_lowercase, ascii_uppercase )
from datetime import datetime, timedelta

import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

import routers.prompts as prompts

#from passlib.context import CryptContext
#bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

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

def get_bool(variable):
    if (isinstance(variable, str) and variable == "yes") or \
        (isinstance(variable, bool) and variable):
        return True
    
    return False

def make_response(message, session_info, intent_name, decision_intent_name, 
                  columns=[], rows=[], sources=[], models=[], 
                  html=None, url=None):
    fulfillment_response = {
        "fulfillment_response": {
            "messages": [{"text": {"text": [message]}}]
        },
        "session_info": session_info,
        "payload": {
            "intent": intent_name, 
            "decision_intent": decision_intent_name,
            "columns": columns,
            "rows": rows,
            "sources": sources,
            "models": models,
            "html": html,
            "url": url
        }
    }

    return fulfillment_response

def generate_others(intent_name, session_info):
    # 비교가 아니거나 비교제품 또는 모델이 없는 경우
    decision_intent_name = "others"
    message = "Mismatching Intent"

    fulfillment_response = make_response(message, session_info, 
                                        intent_name, decision_intent_name)
    print("fulfillment_response", fulfillment_response)
    return fulfillment_response


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
