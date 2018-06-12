from PIL import Image
import pytesseract

img = Image.open('test.png')
# text = pytesseract.image_to_string(Image.open('test.png'), lang='chi_sim')
# print(text)
