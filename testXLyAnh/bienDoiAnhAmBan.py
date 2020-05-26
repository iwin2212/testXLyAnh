import numpy
import cv2

path = r'G:\stock\bean.jpg'
#1:imread_color, 0:imread_grayscale, -1:imread_unchanged
anhGoc = cv2.imread(path, 1)
cv2.imshow("anh goc", anhGoc)
anhMoi = 255-anhGoc
cv2.imshow("anh sau bien doi", anhMoi)
cv2.waitKey(0)