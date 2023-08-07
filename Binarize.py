import cv2
import numpy as np
from matplotlib import pyplot as plt

#Load image
img = cv2.imread('D:\Project OCR\Change_img\hornai-50cm-addcont\hornai-50cm-300-addcont15-1215.jpg')
cv2.imwrite('D:\Project OCR\Change_img\hornai-50cm-addcont\hornai-50cm-300-addcont15-1215.jpg', img)

ret,img1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,img2 = cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
ret,img3 = cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
ret,img4 = cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)

#cv2.imshow("Original",img)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("img3",img3)
cv2.imshow("img4",img4)
plt.imsave('D:/Project OCR/Change_img/SC1.5Bi-1215-1.jpg',img1)
plt.imsave('D:/Project OCR/Change_img/SC1.5Bi-1215-2.jpg',img2)
plt.imsave('D:/Project OCR/Change_img/SC1.5Bi-1215-3.jpg',img3)
plt.imsave('D:/Project OCR/Change_img/SC1.5Bi-1215-4.jpg',img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
