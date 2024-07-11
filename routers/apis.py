from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

import json
import os

import routers.dummy as dummy
from utils import bigqueryapi, postgresqlapi

router = APIRouter(
  prefix="",
  tags=['apis'],
  responses={404: {"description": "Not found"}}
)

@router.get("/")
async def home():
    return {"message": "Hell World"}

@router.post("/weather", response_class=JSONResponse)
async def weather(request: Request):
    print('/weather')

    print('request', request)
    #body = await request.body()
    #print('body', body)
    data = await request.json()
    print('data', data)
    location = data.get("location")
    print('location', location)

    response = {
        "location": location,
        "temperature": 38,
        "description": "Partly Cloudy",
        "icon": "partly-cloudy",
        "humidity": 65,
        "wind": { "speed": 10, "direction": "NW" } 
    }

    return JSONResponse(content=jsonable_encoder(response))


@router.post("/galaxy-spec", response_class=JSONResponse)
async def galaxy_spec(request: Request):
    print('/galaxy-spec')

    print('request', request)
    #body = await request.body()
    #print('body', body)
    data = await request.json()
    print('data', data)
    model = data.get("model")
    print('model', model)

    query = f"""SELECT * FROM `samsung-poc-425503.rubicon_poc.smartphone_spec_2324`
    WHERE `모델코드` LIKE '%{model}%' OR `라인업` LIKE '%{model}%' OR `시리즈` LIKE '%{model}%' OR `상품명` LIKE '%{model}%'
    """

    # BigQuery 연동
    app_dir = os.environ['APP_HOME']
    bigquery_api = bigqueryapi.BigQueryAPI(service_account=f'{app_dir}/credentials/samsung-poc.json')
    dataframe = bigquery_api.query(query)
    print('dataframe', dataframe)

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
    
    #GALAXY, Galaxy, 갤럭시, 갤 -> 유의어 처리부분 필요
    models = ['Galaxy S24', '갤럭시 S24']
    query = f"""SELECT
        *
    FROM
        pivot_spec_s23
    WHERE
        "모델코드" SIMILAR TO '%{'%|%'.join(models)}%' OR
        "라인업" SIMILAR TO '%{'%|%'.join(models)}%' OR
        "시리즈" SIMILAR TO '%{'%|%'.join(models)}%' OR
        "상품명" SIMILAR TO '%{'%|%'.join(models)}%'
    UNION
    SELECT
        *
    FROM
        pivot_spec_s24
    WHERE
        "모델코드" SIMILAR TO '%{'%|%'.join(models)}%' OR
        "라인업" SIMILAR TO '%{'%|%'.join(models)}%' OR
        "시리즈" SIMILAR TO '%{'%|%'.join(models)}%' OR
        "상품명" SIMILAR TO '%{'%|%'.join(models)}%'
    """
    print('query', query)
    row = postgresql_api.query_all(query)
    print(row)

    #response = dummy.galaxy_list_json
    response = dummy.galaxy_list_camera_json
    obj_str = json.dumps(response).replace('__MODEL_ID__', model)
    response = json.loads(obj_str)

    return JSONResponse(content=jsonable_encoder(response))

@router.post("/compare-galaxy-spec", response_class=JSONResponse)
async def compare_galaxy_spec(request: Request):
    print('/compare-galaxy-spec')

    print('request', request)
    #body = await request.body()
    #print('body', body)
    data = await request.json()
    print('data', data)
    model = data.get("model")
    print('model', model)
    if "," in model:
        print('models', model.split(','))

    #response = dummy.galaxy_list_json
    response = dummy.galaxy_list_camera_json
    obj_str = json.dumps(response).replace('__MODEL_ID__', model)
    response = json.loads(obj_str)

    return JSONResponse(content=jsonable_encoder(response))