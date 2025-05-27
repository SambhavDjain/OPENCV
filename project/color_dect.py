
import cv2 as cv 
from project.color_dect_util import get_limits

yellow = [0,255,255]

cap = cv.VideoCapture(0)

while True:

    ret,frame = cap.read()

   
    hsvImage = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lowerlimit,upperlimit = get_limits(color=yellow)

    mask = cv.inRange(hsvImage,lowerlimit,upperlimit)
    
    #FOR MULTIPLE OBJECTS
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
    for cnt in contours:
        area=cv.contourArea(cnt)
        if area >500:
            x1,y1,x2,y2 = cv.boundingRect(cnt)
            cv.rectangle(frame,(x1,y1),(x1+x2,y1+y2),(0,255,0),2)

    contours,_ = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv.contourArea(cnt)>500:
            x1,y1,x2,y2 = cv.boundingRect(cnt)
            frame = cv.rectangle(frame,(x1,y1),(x1+x2,y1+y2),(0,255,0),5)
    
    cv.imshow('frame',frame)


    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    cv.imshow('mask',mask)
cap.release()
cap.destroyAllWindows()


#CHATGPT HELP 
'''
import cv2
from util import get_limits

yellow = [0, 255, 255]  # yellow in BGR
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)


    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 300:  # Adjust as needed
            x1, y1, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)  # helpful for debugging

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''