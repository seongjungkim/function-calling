from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(
  prefix="",
  tags=['apis'],
  responses={404: {"description": "Not found"}}
)

@router.get("/")
async def home():
    return {"message": "Hell World"}

@router.post("/get-weather", response_class=JSONResponse)
async def get_weather(request: Request):
    print('/get-weather')

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