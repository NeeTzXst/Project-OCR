import easyocr

for i in range(1,10):
    IMAGE_PATH = 'D:\Project OCR\Hornai\hornai-50cm-150'+str(i)+'.jpg'
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(IMAGE_PATH, paragraph="False")
    print(IMAGE_PATH)
    print(result)
    print('\n')

for i in range(10,19):
    IMAGE_PATH = 'D:\Project OCR\Hornai\hornai-50cm-15'+str(i)+'.jpg'
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(IMAGE_PATH,paragraph="False")
    print(IMAGE_PATH)
    print(result)
    print('\n')