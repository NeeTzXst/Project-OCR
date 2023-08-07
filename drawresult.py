import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'D:\Project OCR\Hornai-50\hornai-50cm-1101.jpg'

reader = easyocr.Reader(['en'],gpu=False) 
result = reader.readtext(IMAGE_PATH, paragraph = "False")
print(result)

img = cv2.imread(IMAGE_PATH)
spacer = 100
for detection in result: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv2.putText(img,text,(20,spacer), cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,255,0),2,cv2.LINE_AA)
    spacer+=15

plt.figure(figsize=(10,10))
plt.imshow(img)
#plt.imsave('D:\Project OCR\Change_img\Run\hornai-50cm-1105.jpg',img)
plt.show()