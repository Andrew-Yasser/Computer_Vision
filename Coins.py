import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors as clr

img = cv2.imread('coins.jpg', 0)
gray = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

ret, thresh = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)

ker = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (105 , 105))

erosion = cv2.erode(thresh , ker , iterations = 1)
plt.imshow(erosion, cmap='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

big = cv2.dilate(erosion , ker ,iterations = 1)
plt.imshow(big, cmap='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

ker2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
dilbig = cv2.dilate(big,ker2,iterations = 1)
erbig = cv2.erode(big,ker2,iterations = 1)

bigframe = dilbig - erbig
plt.imshow(bigframe, cmap='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

(bigcoin, _) = cv2.findContours(big, cv2.RETR_LIST,
            cv2.CHAIN_APPROX_NONE)

cv2.drawContours(gray, bigcoin, -1, (0, 0, 255), 6)
cv2.imshow("Result", gray)
cv2.waitKey(0)
print("The number of big coins is %i " % len(bigcoin))

presm = thresh - big
plt.imshow(presm, cmap='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

ker1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))
erpre = cv2.erode(presm,ker1,iterations = 1)
plt.imshow(erpre, cmap='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

small = cv2.dilate(erpre,ker1,iterations = 1)
plt.imshow(small, cmap='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

ker3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
dilsmall = cv2.dilate(small,ker3,iterations = 1)
ersmall = cv2.erode(small,ker3,iterations = 1)
smframe=  dilsmall - ersmall
plt.imshow(smframe, cmap='gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

(smallcoin, _) = cv2.findContours(small, cv2.RETR_LIST,
            cv2.CHAIN_APPROX_NONE)


cv2.drawContours(gray, smallcoin, -1, (255, 0, 0), 6)
cv2.imshow("Result", gray)
cv2.waitKey(0)
print("The number of small coins is %i " % len(smallcoin))
h = len(smallcoin)*50 + len(bigcoin)*100
print("The total in the picture is %dh cents" % h)
