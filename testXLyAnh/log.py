import numpy
import cv2
import math

path = r'G:\stock\bean.jpg'
#1:imread_color, 0:imread_grayscale, -1:imread_unchanged
anhGoc = cv2.imread(path, 0)
cv2.imshow("anh goc", anhGoc)
print(anhGoc)

a, b = anhGoc.shape

for i in range(a):
    for j in range(b):
        anhGoc[i][j] = (int)( 10* math.log(1 + anhGoc[i][j])) # ham logarit
        #anhGoc[i][j] = pow(10, 1 + anhGoc[i][j]) # ham log nguoc
print(anhGoc)
cv2.imshow("anh sau", anhGoc)
cv2.waitKey(0)