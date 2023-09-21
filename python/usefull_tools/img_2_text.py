#!/usr/bin/python3

#pip install opencv-python
#pip install pytesseract
#sudo apt update
#sudo apt install tesseract-ocr
#sudo apt install libtesseract-dev

import pytesseract
import cv2
import sys

try:
	image_name = sys.argv[1]
except:
	print('Usage: ./img_2_text.py image_name')
	sys.exit()
	
image = cv2.imread(image_name)	# reads the image

# text = pytesseract.image_to_pdf_or_hocr test this later
text = pytesseract.image_to_string(image)
print(text)
