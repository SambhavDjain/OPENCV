import cv2

#READ WEBCAM 

webcam = cv2.VideoCapture(0)

#VISUALIZE WEBCAM 

while True:

    ret,frame = webcam.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xFF ==ord('q'):#To exits from the webcam need to press ' q '
        break


webcam.release()
cv2.destroyAllWindows()
