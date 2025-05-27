#import libraries

import cv2 as cv 

#START CAMERA
cap = cv.VideoCapture(0)

#LOAD FACE DETECTOR
face_dect = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
#cv.CascadeClassifier(...):loads a pre-trained classifier
#cv.data.haarcascades -> points to the directory within the OpenCV library where these classifier stored


while True:
    ret,frame = cap.read()
    if not ret:
        break

    #ON CONVERTING IT TO GRAYSCALE
    cap_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    #DETECTION OF FACES

    faces = face_dect.detectMultiScale(cap_gray,1.1,4)
    '''1.1 means the image is reduced by 10% at each scale thus on reducing it it gives more accurate and fine results
    but also increase computational time 
    3-6 is good if 3  more face detect but some amy be wrong 
    5 or 6 fewer bot more confident or precise detections''' 

    #BLUR EACH FACE
    for (x,y,w,h) in faces:
        faces = frame[y:y+h,x:x+w]
        blur = cv.GaussianBlur(faces, (51,71),10)
        '''Here the 51 ,21 are the width and height 
        both has to be odd and positive 
        and the 30 is the value by which bluring occurs more 
        value means more blur'''
        frame[y:y+h,x:x+w] = blur
        cv.rectangle(frame, (x,y),(x+w,y+h),(0, 255, 0), 3)
    #show result
    cv.imshow('Anonymizer',frame)

    #To exit 
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

