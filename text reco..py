from PIL import Image
from pytesseract import pytesseract
from gtts import gTTS
import os
import time

img = Image.open("I.jpg")
pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")

Mtext = pytesseract.image_to_string(img)
print(Mtext)
language ='en'
obj =gTTS(text = Mtext,lang=language)    # convert text into voice
obj.save("D.mp3")
time.sleep(2)
os.system("D.mp3")                          # voice output
