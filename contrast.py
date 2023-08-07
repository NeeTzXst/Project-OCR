import cv2
from matplotlib import pyplot as plt

img = cv2.imread('D:\Project OCR\Hornai\hornai-50cm-1112.jpg')

contrast = 1
brightness1 = 50
brightness2 = -50

contrast_img = cv2.convertScaleAbs(img,alpha = contrast,beta = brightness2)

#cv2.imshow("Original",img)
cv2.imshow("contrast",contrast_img)
plt.imsave('D:/Project OCR/Change_img/Con_1112.jpg',contrast_img)
cv2.waitKey(0)
cv2.destroyAllWindows()