#convert a grayscale image into a binary image (black and white) by choosing a threshold value.


import cv2 as cv 
import os

img = cv.imread(os.path.join('.','Photo','bear.jpg'))


img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret , thresh = cv.threshold(img_gray,80,255, cv.THRESH_BINARY)
#Pixels > 80 → set to 255 (white)
#Pixels ≤ 80 → set to 0 (black)


thresh = cv.blur(thresh,(10,10))
ret , thresh = cv.threshold(thresh,80,255, cv.THRESH_BINARY)


cv.imshow('img_grey',img_gray)
cv.imshow('thresh',thresh)

#cv.imshow('img',img)
cv.waitKey(0)