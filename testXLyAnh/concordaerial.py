import cv2
import numpy

path = r"‪G:\stock\concordaerial.png"

A = cv2.imread(path);
Ref = cv2.imread(path, 0);
B = cv2.imhistmatch(A,Ref);
cv2.imshow("RGB_Image_with_Color_Cast", A)
cv2.imshow("Reference_Grayscale_Imaget", Ref)
cv2.imshow("Histogram_Matched_RGB_Image", B)


