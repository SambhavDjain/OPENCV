import os
import cv2 

#READ VIDEO

video_path = os.path.join('.','Video','monkey.mp4')

video = cv2.VideoCapture(video_path)

#VISUALIZE VIDEO

ret = True

while ret:
    ret,frame = video.read()

    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(10)

video.release()#Frees up memory,Closes the video file properly.
cv2.destroyAllWindows()#"Close all the image/video windows I opened."