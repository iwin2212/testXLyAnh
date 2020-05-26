import numpy
import cv2
import math

path = r'G:\stock\bean.jpg'
#1:imread_color, 0:imread_grayscale, -1:imread_unchanged
anhGoc = cv2.imread(path, 0)
cv2.imshow("anh goc", anhGoc)

a, b = anhGoc.shape

for i in range(a):
    for j in range(b):
        anhGoc[i][j]=10*(pow(anhGoc[i][j]+1, 0.4))

cv2.imshow("anh sau bien doi", anhGoc)
cv2.waitKey(0)
