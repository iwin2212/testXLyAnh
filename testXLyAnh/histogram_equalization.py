import numpy as np
import cv2
from matplotlib import pyplot as plt

path = r"C:\Users\bacht\Desktop\profile.jpg"

test_img = cv2.imread(path, -1)

hist, bins = np.histogram(test_img.flatten(), 256, [0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

cv2.imshow("original img", test_img)
plt.plot(cdf_normalized, color = 'b')
plt.hist(test_img.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper_left')
plt.show()