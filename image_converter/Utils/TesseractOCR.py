import cv2

from PIL import Image

import pytesseract

#pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import numpy as np

from pytesseract import Output



filename = '01.jpg'
img = np.array(Image.open(filename))

result = pytesseract.image_to_string(img,lang='fas')

with open('image.txt',mode="w",encoding="utf-8") as text:
    text.write(result)
    print(result)

