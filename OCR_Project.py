
import cv2 
import pytesseract as ocr
ocr.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("sample5.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY_INV) # threshold:any value of a puxel smaller than 100 will be black
cv2.imshow("processed image",thresh)


os = open("result.txt", "w+") 
os.write("") 
os.close() 
result = open("result.txt", "a") 
custom_config = r'--oem 3 --psm 6'
text_result = ocr.image_to_string(thresh, config=custom_config)
print(text_result)
result.write(text_result)  
# Close the file 
result.close() 


#to count number of charachters without spaces
print(len(text_result) - (text_result.count(' ') + text_result.count('\n') + text_result.count('')))


cv2.waitKey(0)
cv2.destroyAllWindows()
