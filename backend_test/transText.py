import whisper
from enum import Enum

class ModelType(Enum):
  BASE="base"
  SMALL="small"
  MEDIUM = "medium"
  LARGE="large"

  
def TransText(level:ModelType,voiceFile):
  # 追々levelもこっちの引数にする。
  # model = whisper.load_model(level)
  model = whisper.load_model(level)
  result = model.transcribe(voiceFile,fp16=False)
  return result['text']