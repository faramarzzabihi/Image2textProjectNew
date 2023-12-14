from paddleocr import PaddleOCR
ocr = PaddleOCR(lang='fa')
result = ocr.ocr('01.jpg')

y=10
text=""
line_text=""
#Print the result
for line in result:
  print(line)
  print( line[0][0][1])
  if abs(line[0][0][1]-y) <10:
    line_text=line[1][0]+' '+line_text
  else:
    text+=line_text
    line_text='\n'
    y=line[0][0][1]
text+=line_text
  #print(line[0][2])
# draw result
with open('text_paddle.txt', 'w') as f:
    f.write(text)

from PIL import Image
from paddleocr import PaddleOCR,draw_ocr
image = Image.open('01.jpg').convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='B-NAZANIN.TTF')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')