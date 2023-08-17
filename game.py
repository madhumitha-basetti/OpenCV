import numpy as np
import random
import time
import cv2
img=np.zeros([512,512,3],np.uint8)
cv2.namedWindow('image')
l=[]
        
def nothing(x):
    print(x)
switch='0:Off_1:On'
cv2.createTrackbar(switch,'image',0,1,nothing)
while(1):
    s=cv2.getTrackbarPos(switch,'image')
    if s==0:
        pass
    else:
        if s==0:
            pass
        else:
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'madhu',(225,225),font,4,(255,255,255))
            
    cv2.imshow('image',img)
    k=cv2.waitKey(0)
    if k & 0xFF==ord('q'):
        break
    
