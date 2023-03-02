from fastapi import FastAPI, File, UploadFile, Form
import shutil
from transText import ModelType,TransText
from tempfile import NamedTemporaryFile
from pathlib import Path

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
      print(type(fileb))  # <class 'starlette.datastructures.UploadFile'>
      print(type(fileb.file)) #<class 'tempfile.SpooledTemporaryFile'>
      suffix = Path(fileb.filename).suffix  # 拡張子の取得
      with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
          shutil.copyfileobj(fileb.file, tmp)
          print(tmp.name)
          tmp_path = Path(tmp.name)
          print(tmp_path)
          print("**********")
          # t = TransText(ModelType.BASE,tmp_path)
  finally:
      fileb.file.close()
  return {
      "filename": fileb.filename,
      "temporary_filepath": tmp_path,
      "token": token,
      "fileb_content_type": fileb.content_type,
      # "text":text
  }