from fastapi import FastAPI, File, UploadFile, Form
from transText import ModelType,TransText

app = FastAPI()

@app.get("/api/hello")
async def get_hello():
    return {"message" : "Hello,World"}
  
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