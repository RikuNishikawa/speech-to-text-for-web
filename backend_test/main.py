from fastapi import FastAPI, File, UploadFile, Form
import shutil
from transText import ModelType,TransText
from tempfile import NamedTemporaryFile
from pathlib import Path
import os
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
  "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/api/{message}")
def get_any_message(message: str):
  return {"message": message}

@app.post("/uploadtest/")
async def test(file: UploadFile = File(...)):
  contents = await file.read()
  print(contents)
  print("ok")
  return {"message": "success"}
