import os
import cv2 as cv 

img = cv.imread(os.path.join('.','Photo','dogs.jpg'))

resized_img = cv.resize(img, (960,960))

print(img.shape)

cv.imshow('img',img)
cv.imshow('resized_img',resized_img)

cv.waitKey(0)

