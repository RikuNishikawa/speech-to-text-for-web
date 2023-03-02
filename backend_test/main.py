from fastapi import FastAPI, File, UploadFile, Form
import shutil
from transText import ModelType,TransText
from tempfile import NamedTemporaryFile
from pathlib import Path
import os

app = FastAPI()
  
@app.get("/api/{message}")
def get_any_message(message: str):
  return {"message": message}

@app.post("/uploadfile/")
async def post_upload_file(file:UploadFile=File(...)):
  # whisperに音声ファイルを投げる
  # text = TransText(ModelType.BASE,file)
  # return textdata
  # print(text)
  return {"filename": file.filename,"filesize":file.size,"headers":file.headers,"file.file":file.file}

@app.post("/saveuploadfile/")
async def save_upload_file_tmp(fileb: UploadFile=File(...), token:str=Form(...)):
  tmp_path:Path = ""
  try:
      # print(type(fileb))  # <class 'starlette.datastructures.UploadFile'>
      # print(type(fileb.file)) #<class 'tempfile.SpooledTemporaryFile'>
      suffix = Path(fileb.filename).suffix  # 拡張子の取得
      # tmpfile = NamedTemporaryFile(mode='r',suffix=suffix)
      path = f'./tmp/{fileb.filename}'
      with open(path,'w+b') as buffer:
        shutil.copyfileobj(fileb.file,buffer)
        print("**********")
        text = TransText(ModelType.BASE.value,path)
        print("**********")
        # print(t)
      # with NamedTemporaryFile(delete=False, suffix=suffix) as tmpfile:
      #     shutil.copyfileobj(fileb.file, tmpfile)
      #     fileb.file.write()
      #     print("tmpfile",tmpfile)
      #     # tmpfile.write()
      #     tmp_path = Path(tmpfile.name)
      #     # print(tmp_path)
  finally:
      fileb.file.close()
      os.remove(path=path)
  return {
      "filename": fileb.filename,
      "text":text,
      "filesize": fileb.size,
      "temporary_filepath": tmp_path,
      "token": token, # なんでtokenが必要なのかよくわかっていない
      "fileb_content_type": fileb.content_type,
  }