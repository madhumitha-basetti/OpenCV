import cv2
t=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
print(t.isOpened())
while(t.isOpened()):
    ret,frame=t.read()
    if ret==True:
        out.write(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) &0xFF==ord('q'):
            break
    else:
        break
t.release()
out.release()
cv2.destroyAllWindows()
