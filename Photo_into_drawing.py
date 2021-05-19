import cv2
import numpy as np
from matplotlib import pyplot as plt
img = plt.imread('2.jpeg') #choose the path of the picture here.
plt.imshow(img) #showing the original photo
plt.title('original') #making a title to the original photo


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #make the img to grayscale image
plt.imshow(gray, cmap='gray') #to plot in grayscale

invertedGray = 255 – gray #obtain negative of the grayscale picture (light areas of the picture 
become dark)
plt.imshow(invertedGray, cmap='gray') #to plot in grayscale
blur = cv2.GaussianBlur(invertedGray, (21,21),0) #gaussian blur to decrease noise in pic
plt.imshow(blur, cmap='gray') #to plot in grayscale

invertedBlur = 255 – blur #obtain negative of the blurred pic
plt.imshow(invertedBlur, cmap='gray') #to plot in grayscale
finalImg = cv2.divide(gray, invertedBlur, scale = 250.0)

plt.imshow(finalImg, cmap='gray') #to plot result 
plt.imshow(img) #to plot original
