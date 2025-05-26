import os
import cv2 as cv 

img =  cv.imread(os.path.join('.','Photo','Whiteboard.jpg'))
resized_img= cv.resize(img,(960,900))

print(resized_img.shape)
#LINE 
line =  cv.line(resized_img,(200,350),(500,550),(0,255,0),3)
#100,150 and 300,450 are x and y coordinates thus 0,255,0 refers green colour and 3 is the thickness 

#RECTANGLE 
rectangle = cv.rectangle(resized_img,(800,400),(400,700),(255,0,0),4)

#CIRCLE
cv.circle(resized_img,(300,350),140,(0,0,255),5)
#500,8000 are x,y coordinates ,140 is radius aand rest knopwn


#TEXT
cv.putText(resized_img,'Hey You',(200,400),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(255,255,0),4)
# in this just 2 is the font size 



#cv.imshow('img',img)
cv.imshow('resized_img',resized_img)
cv.waitKey(0)