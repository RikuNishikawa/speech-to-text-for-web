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
def get_any_message(message):
  return {"message": message}

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
  filename = file.filename
  path = f'./tmp/{file.filename}'
  try:
    with open(path,'w+b') as buffer:
          shutil.copyfileobj(file.file,buffer)
          text = TransText(ModelType.BASE.value,path)
  finally:
    filename = os.path.splitext(os.path.basename(path))[0]
    # textpath = f"./tmp/{filename}.txt"
    # with open(textpath,"w") as f:
    #   f.write(text)
    file.file.close()
    os.remove(path=path)
  print("ok")
  return {"stuta": "success", "text" : text, "filename" : filename}

@app.get("/textfile/")
async def getTextFile():
    
    return "aaa"
