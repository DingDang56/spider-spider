# #orc技术识别图形验证，光学字符识别
# # pip install tesseract
#
# from pytesseract import image_to_string
# tessdata_dir_config = '--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'
# from PIL import Image
# # #
# image = Image.open('index.png')
# result = image_to_string(image)
# print(result)

from PIL import Image
from pytesseract import image_to_string

tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'
img = Image.open("1.png")
text = image_to_string(img,lang = 'chi_sim',config=tessdata_dir_config)#eng 英文，chi_sim中文,
print(text)
# import hashlib
#
# pas= "7829"
# password = hashlib.md5()
# a = password.update(pas.encode())
# s= password.hexdigest()
# print(s)