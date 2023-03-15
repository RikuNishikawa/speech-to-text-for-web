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

@app.post("/uploadtest/")
async def test(file: UploadFile = File(...)):
  filename = file.filename
  path = f'./tmp/{file.filename}'
  try:
    with open(path,'w+b') as buffer:
          shutil.copyfileobj(file.file,buffer)
          text = TransText(ModelType.BASE.value,path)
  finally:
    file.file.close()
    os.remove(path=path)
  print(filename)
  print("ok")
  return {"stuta": "success","text" : text}

@app.post("/saveuploadfile/")
async def save_upload_file_tmp(fileb: UploadFile=File(...)):
  # tmp_path:Path = ""
  print(fileb)
  try:
      # print(type(fileb))  # <class 'starlette.datastructures.UploadFile'>
      # print(type(fileb.file)) #<class 'tempfile.SpooledTemporaryFile'>
      suffix = Path(fileb.filename).suffix  # 拡張子の取得
      path = f'./tmp/{fileb.filename}'
      with open(path,'w+b') as buffer:
        shutil.copyfileobj(fileb.file,buffer)
        print("**********")
        print(path,os.path.exists(path))
        text = TransText(ModelType.BASE.value,path)
        print("**********")
      # tmpfile = NamedTemporaryFile(mode='r',suffix=suffix)
      # with NamedTemporaryFile(delete=False, suffix=suffix) as tmpfile:
      #     shutil.copyfileobj(fileb.file, tmpfile)
      #     fileb.file.write()
      #     print("tmpfile",tmpfile)
      #     # tmpfile.write()
      #     tmp_path = Path(tmpfile.name)
      #     # print(tmp_path)
  finally:
      fileb.file.close()
      #os.remove(path=path)
  return {
      "filename": fileb.filename,
      "text":text,
      "filesize": fileb.size,
      # "temporary_filepath": tmp_path,
      "fileb_content_type": fileb.content_type,
  }