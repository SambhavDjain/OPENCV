
import cv2 as cv 
from color_dec_util import get_limits

yellow = [0,255,255]

#Start camera
cap = cv.VideoCapture(0)

while True:

    ret,frame = cap.read()

   # convert img to hsv
    hsvImage = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    #Uses custom function to get HSV range for the yellow color
    lowerlimit,upperlimit = get_limits(color=yellow)
    #Crete mask - a binary image which contains only 0s blacks and 255s whites
    mask = cv.inRange(hsvImage,lowerlimit,upperlimit)
    
    #FOR MULTIPLE OBJECTS
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
    for cnt in contours:
        area=cv.contourArea(cnt)
        if area >500: #	Filter small obj (too small to be object)
            x1,y1,w,h = cv.boundingRect(cnt)#w ,h are width and height
            cv.rectangle(frame,(x1,y1),(x1+w,y1+h),(0,255,0),2)
            
    #To show the output
    cv.imshow('frame',frame)

    #To exit 
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    cv.imshow('mask',mask)
cap.release()
cap.destroyAllWindows()

