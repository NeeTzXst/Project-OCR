import easyocr

IMAGE_PATH = 'D:\Project OCR\Hornai\hornai-50cm-1512.jpg'
reader = easyocr.Reader(['en'], gpu = False)
result = reader.readtext(IMAGE_PATH,paragraph="False")

print(result)
    