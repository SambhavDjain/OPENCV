import cv2 as cv 
import os 


img = cv.imread(os.path.join('.','Photo','cow.jpg'))


k_size = 7 #Its the intensity how much it got blurred 
img_blur = cv.blur(img,(k_size,k_size))
img_g_blur = cv.GaussianBlur(img,(k_size,k_size),3)
img_median_blur = cv.medianBlur(img,k_size)

cv.imshow('img',img)
cv.imshow('img_median_blur',img_median_blur)
#cv.imshow('img_g_blur',img_g_blur)

#cv.imshow('img_blur',img_blur)

cv.waitKey(0)