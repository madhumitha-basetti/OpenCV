import numpy as np
import cv2
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        color_image=np.zeros([512,512,3],np.uint8)
        color_image[:]=[blue,green,red]
        cv2.imshow('color',color_image)
img=cv2.imread('E:/python/OpenCV/lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
