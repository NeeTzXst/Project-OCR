import cv2
import numpy as np
from matplotlib import pyplot as plt

#Load image
input = cv2.imread('D:\Project OCR\Hormai-60\hornai-60cm-191221-All\hornai-60cm-1105.jpg',0)

img = cv2.cvtColor(input,cv2.COLOR_BAYER_BG2GRAY)

#blur image
blurred_img = cv2.GaussianBlur(img,(1,1),0)

#adaptive image
adp_img = cv2.adaptiveThreshold(blurred_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

rimg = cv2.resize(img, (800, 800))
radp_img = cv2.resize(adp_img, (750, 750))
cv2.imshow("Original",img)
cv2.imshow("GRAY",img)
#cv2.imshow("Adaptive Threshold ",radp_img)
#plt.imsave('D:/Project OCR/Change_img/bina-1105.jpg',adp_img)
#plt.savefig('D:/Project OCR/Change_img/bina-1105.jpg')
cv2.waitKey(0)
cv2.destroyAllWindows()
