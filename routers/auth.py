from fastapi import Depends, HTTPException, status, APIRouter, Request, Response, Form

router = APIRouter(
  prefix="/chat",
  tags=["auth"],
  responses={401: {"user": "Not authorized"}}
)