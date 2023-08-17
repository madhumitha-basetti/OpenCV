import cv2
img=cv2.imread('E:/python/OpenCV/messi5.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
img2=cv2.imread('E:/python/OpenCV/opencv-logo.png')
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
img=cv2.resize(img,[512,512])
img2=cv2.resize(img2,[512,512])
new=cv2.add(img,img2)
img3=cv2.addWeighted(img,.5,img2,.5,0)
cv2.imshow('image',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
