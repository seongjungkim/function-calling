# main.py

import datetime
import io
import os
import uuid

from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from routers import auth, apis, views, chatbot

from google.cloud import storage

app = FastAPI()

app.include_router(auth.router)
app.include_router(views.router)
app.include_router(apis.router)
app.include_router(chatbot.router)
