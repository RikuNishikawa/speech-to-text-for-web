import whisper
from enum import Enum

class ModelType(Enum):
  BASE="base"
  SMALL="small"
  MEDIUM = "medium"
  LARGE="large"

# class TransText():
#   '''
#   modelの種類: ↑計算量小、精度低
#     base
#     small
#     medium
#     large
#   '''
#   def __init__(self):
#     # self.level = level
#     pass  
  
def TransText(level:ModelType,voiceFile):
  # 追々levelもこっちの引数にする。
  model = whisper.load_model(level)
  result = model.transcribe(voiceFile)
  return result