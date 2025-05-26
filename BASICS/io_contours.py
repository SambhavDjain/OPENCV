import os 
import cv2 as cv 

img = cv.imread(os.path.join('.','Photo','birdflying.jpg'))

img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img_gray,125,200,cv.THRESH_BINARY_INV)
#INV means inverse


contours ,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv.contourArea(cnt) > 100: #"Only detect shapes (like birds) that cover more than 100 pixels."
        #cv.drawContours(img,cnt,-1,(0,255,0),1)
        x1,y1,w,h = cv.boundingRect(cnt)#x1, y1 = top-left corner of the rectangle. w, h = width and height



        cv.rectangle(img,(x1,y1),(x1+w ,y1+h),(0,255,0),2)

cv.imshow('img',img)
cv.imshow('img_gray',img_gray)
cv.imshow('thresh',thresh)

cv.waitKey(0)