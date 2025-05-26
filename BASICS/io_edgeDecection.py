#EDGES DETECTION 

import os
import cv2 as cv
import numpy as np 



img = cv.imread(os.path.join('.','Photo','basketballplayer.jpg'))

img_edge = cv.Canny(img,100,200)# edge detection algorithm here 100 and 200 useed to get the perfect outline image it can be varied 


#DILATE ->Dilation means growing the white areas in a black-and-white (binary) image.
img_edge_d = cv.dilate(img_edge,np.ones((3,3),dtype = np.int8))

#ERODE
#It helps to make the dilate image more shrink  and  white areas in the image.
img_edge_e=cv.erode(img_edge_d,np.ones((3,3),dtype = np.int8)) 


cv.imshow('img_edge',img_edge)
cv.imshow('img_edge_d',img_edge_d)
cv.imshow('img_edge_e',img_edge_e)
cv.imshow('img',img)
cv.waitKey(0)