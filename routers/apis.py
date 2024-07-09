from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

import json
import routers.dummy as dummy

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

    response = dummy.galaxy_list_json
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

    response = dummy.galaxy_list_json
    obj_str = json.dumps(response).replace('__MODEL_ID__', model)
    response = json.loads(obj_str)

    return JSONResponse(content=jsonable_encoder(response))