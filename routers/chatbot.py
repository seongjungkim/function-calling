from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, Response, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from core import schemas

# Dummy Data
import routers.dummy as dummy

import json

router = APIRouter(
  prefix="/chatbot",
  tags=['chatbot'],
  responses={404: {"description": "Not found"}}
)
