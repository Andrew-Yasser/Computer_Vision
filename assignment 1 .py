import cv2
import numpy as np
from matplotlib import pyplot as plt
img= plt.imread('Input.jpg')
plt.imshow(img)
plt.title('original')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(gray,5)
plt.imshow(median, cmap='gray')
plt.title('median')
equ= cv2.equalizeHist(median)
plt.imshow(equ, cmap='gray')
plt.title('Histogram Equalization')
thresh = cv2.adaptiveThreshold( median 
,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
 cv2.THRESH_BINARY,11,2)
plt.imshow(thresh, cmap='gray')
plt.title('Adaptive Thresholding “on grayscale”')
sharp=cv2.GaussianBlur(median,(5,5),0)
cv2.blur(median, (5,5))
plt.imshow(sharp, cmap='gray')
plt.title('Sharpening')