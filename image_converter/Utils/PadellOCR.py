from paddleocr import PaddleOCR
import numpy as np
from PIL import Image

def PaddleOCRT2I(img,LineSize):
    
  ocr = PaddleOCR(lang='fa')
  result = ocr.ocr(img)

  #LineSize=10
  text=""
  line_text=""
  for line in result:
    if abs(line[0][0][1]-LineSize) <10:
      line_text=line[1][0]+' '+line_text
    else:
      text+=line_text
      line_text='\n'
      yLineSize=line[0][0][1]
  text+=line_text
  return text