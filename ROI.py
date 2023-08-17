import cv2
import numpy as np
img=cv2.imread('E:/python/OpenCV/messi5.jpg')
cv2.imshow('image',img)
ball=img[280:340,330:390]
img[273:333,100:160]=ball
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




##
##The co-ordinates used in the array follow the format of 
##img [y1: y2, x1: x2]
##Therefore, when copying to another part of the image, you need to ensure that (y2-y1) value remains the same, as well as (x2-x1)
##
##Here's another example to copy messi's head, where Top left coordinates is (200, 60) and bottom right is (270, 140) in x,y format
##
##messi_head = img[60:140, 200:270]
##img[260:340,100:170] = messi_head
##



