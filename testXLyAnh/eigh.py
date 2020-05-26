import numpy as np
import cv2
from numpy import linalg

bean_img = cv2.imread(r"G:\stock\bean.jpg", 1) #1:imread_color, 0:imread_grayscale, -1:imread_unchanged
cv2.imshow("bean", bean_img)
cv2.waitKey(0)

A = np.array([[2,1],[1,2]])
print(A)
A+=A
print(A)

B = np.asarray([[2,1],[1,2]])
print(B)
B+=B
print(B)

triRieng, vectorRieng = linalg.eigh(A)
print(" tri rieng: \n", triRieng)
print("vector rieng: \n", vectorRieng)
# ma tran vuong A (mxm) co m eigenvalues thi m eigenvectors tuong ung, truc giao voi nhau