import cv2 
import pytesseract as ocr
ocr.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
#reading the sample image
img = cv2.imread("sample1.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY_INV) 
#threshold:any value of a pixel smaller than 200 will be black


#showing the image after operations
cv2.imshow("processed image",thresh)
cv2.waitKey(0)
os = open("result.txt", "w+") 
os.write("") 
os.close() 
result = open("result.txt", "a") 
custom_config = r'--oem 3 --psm 6'


#applying the ocr function
text_result = ocr.image_to_string(thresh, config=custom_config)
print(text_result)
result.write(text_result) #writing the the result into the text file
result.close()
#counting the number of charecters excluding spaces and new lines
print(len(text_result) - (text_result.count(' ') + text_result.count('\n') ))

cv2.waitKey(0)
cv2.destroyAllWindows()
