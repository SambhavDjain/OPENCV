import os 
import cv2 as cv 

img = cv.imread(os.path.join('.','Photo','handwritten.jpg'))
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

adaptive_thresh = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21 ,30)
ret, simple_thresh =cv.threshold(img_gray,80,255,cv.THRESH_BINARY)



#cv.ADAPTIVE_THRESH_GAUSSIAN_C -> uses blurrred average of nearby pixels =>Uses a different threshold for each pixel, based on its local neighborhood.local average type
#20-> block size must be odd 
#Higher 30 → more black areas (image looks darker)
#Lower 30 → more white areas
#Sumple_threshold -> Use one fixed value for the whole image.  Global value



cv.imshow('simple_thresh',simple_thresh)
cv.imshow('adaptive_thresh',adaptive_thresh)
cv.imshow('img',img)
cv.waitKey(0)