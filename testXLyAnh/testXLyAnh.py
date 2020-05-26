
import cv2
import numpy

path = r"C:\Users\bacht\Desktop\bean.jpg"
img=cv2.imread(path)
gray=cv2.imread(path, 0)

def TuyentinhTungKhuc(I,r1, s1, r2, s2):
    a,b = I.shape
    for i in range(a):
        for j in range(b):
            if(I[i][j]<=r1):
                I[i][j] = (I[i][j]/r1)*s1
            elif(I[i][j]>= r2):
                I[i][j] = (I[i][j]/r2)*s2
            else:
                I[i][j] =  (I[i][j]-r2)/(225-r2)*(225 - s2)+(I[i][j]-r1)/(225-r1)*(225 - s1)
    cv2.imshow("image2",I)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

cv2.imshow("image1", img)
TuyentinhTungKhuc(gray,60,30,150,200)