import cv2 as cv 
import os

img = cv.imread(os.path.join('.','Photo','dogs.jpg'))

print(img.shape)

cropped_img = img[220:950, 200:840]

#840 increase the right side width 

cv.imshow('img',img)
cv.imshow('cropped_img',cropped_img)

cv.waitKey(0)