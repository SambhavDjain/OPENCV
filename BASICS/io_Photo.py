import os

import cv2 

#Read Image 

image_path = os.path.join('.', 'Photo', 'bird.jpg')

img = cv2.imread(image_path)


#WRITE IMAGE 

cv2.imwrite(os.path.join('.', 'Photo', 'bird_out.jpg'),img) #The path includes  Looking for bird.jpg in a folder named 'Photo'

#VISUALIZE IMAGE
cv2.imshow('image',img)

cv2.waitKey(0)#if i put 5000 insted of 0(0 is infinite time ) annd 5000 is finite time and its in miliseconds 



