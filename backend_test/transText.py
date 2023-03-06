import whisper
from enum import Enum
import os

class ModelType(Enum):
  BASE="base"
  SMALL="small"
  MEDIUM = "medium"
  LARGE="large"

  
def TransText(level:ModelType,voiceFile):
  # 追々levelもこっちの引数にする。
  # model = whisper.load_model(level)
  model = whisper.load_model(level)
  print(voiceFile,os.path.exists(voiceFile))
  result = model.transcribe(voiceFile,fp16=False)
  return result['text']

TransText(ModelType.BASE.value,r"C:\Users\shibata\Documents\konfesu\speech-to-text-for-web\backend_test\tmp\voicetest.mp3")