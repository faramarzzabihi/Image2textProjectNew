from paddleocr import PaddleOCR
import numpy as np
from PIL import Image

def PaddleOCRT2I(img,LineSize,lng):
  if lng=='fas':lng='fa'
  if lng=='eng':lng='en'
  ocr = PaddleOCR(lang=lng)
  result = ocr.ocr(np.array(img))

  yLineSize=LineSize
  text=""
  line_text=""
  for line in result:
    if abs(line[0][0][1]-yLineSize) <LineSize:
      line_text=line[1][0]+' '+line_text
    else:
      text+=line_text
      line_text='\n'
      yLineSize=line[0][0][1]
  text+=line_text
  return text