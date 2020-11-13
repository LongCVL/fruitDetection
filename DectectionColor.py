import cv2
import numpy as np

img = cv2.imread('papaya-fruit.jpg')
#img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_Gauss= cv2.GaussianBlur(img,(7,7),0)
img_hsv = cv2.cvtColor(img_Gauss,cv2.COLOR_BGR2HSV)

# lower = np.array([0,50,50])#lower_qpple
# upper = np.array([10,255,255])#upper_apple
# lower = np.array([0,120,90])#lower_berry+tomato
# upper = np.array([10,255,255])#upper_berry+tomato
lower = np.array([0,110,180])#lower_papaya
upper = np.array([26,255,255])#upper_papaya



mask = cv2.inRange(img_hsv,lower,upper)

kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
result = cv2.bitwise_and(img,img, mask=mask)

cv2.imshow('image',img)
cv2.imshow('result',result)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()