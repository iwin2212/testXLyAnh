import numpy as np
import cv2

path = r"C:\Users\bacht\Desktop\profile.jpg"

test_img = cv2.imread(path, 0)
#histEqualImg = cv2.equalizeHist(test_img)
#res = np.hstack((test_img, histEqualImg)) # stacking images side-by-side
#cv2.imshow("histEqualImg", res)
#cv2.waitKey(0)
#cv2.imwrite("res.png", res)

# It is true that the background contrast has improved after histogram equalization. 
# But compare the face of statue in both images. We lost most of the information there due to over-brightness. 
# It is because its histogram is not confined to a particular region as we saw in previous cases (Try to plot histogram of input image, you will get more intuition).
# So to solve this problem, adaptive histogram equalization is used
# In this, image is divided into small blocks called “tiles” (tileSize is 8x8 by default in OpenCV).
# Then each of these blocks are histogram equalized as usual.So in a small area, histogram would confine to a small region (unless there is noise).
# If noise is there, it will be amplified. To avoid this, contrast limiting is applied. 
# If any histogram bin is above the specified contrast limit (by default 40 in OpenCV), 
# those pixels are clipped and distributed uniformly to other bins before applying histogram equalization. 
# After equalization, to remove artifacts in tile borders, bilinear interpolation is applied.

# create a CLAHE object (Arguments are optional). CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
imgAfterClahe = clahe.apply(test_img)
attachImg = np.hstack((test_img, imgAfterClahe))
cv2.imshow("img", attachImg)
cv2.waitKey(0)