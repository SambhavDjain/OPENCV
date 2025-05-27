import numpy as np 
import cv2 as cv


yellow = [0,255,255] #Yellow in bgr color space 


def get_limits(color):

    c = np.uint8([[color]]) #insert bgr values which u want to convert to hsv 

    hsvC = cv.cvtColor(c,cv.COLOR_BGR2HSV)

    lowerlimit = hsvC[0][0][0]- 10,90,90
    upperlimit = hsvC[0][0][0]+ 10,255,255
    

    
    lowerlimit = np.array(lowerlimit,dtype = np.uint8)
    
    upperlimit = np.array(upperlimit,dtype = np.uint8)
    

    return lowerlimit,upperlimit