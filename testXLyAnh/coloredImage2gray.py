import cv2
import numpy
import os

#import image
path = 'C:/Users/bacht/Desktop/100k/1k'



#method walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up.

#os.path.join(path, *paths)
#path: A path-like object representing a file system path.
#*path: A path-like object representing a file system path. It represents the path components to be joined.
#A path-like object is either a string or bytes object representing a path.


#đọc file ảnh màu từ thư mục
files = []
#r=root, d=directories, f=files
for r, d, f in os.walk(path):
  for file in f:
    if '.jpg' in file:
      files.append(os.path.join(r, file))

#chuyển sang ảnh đen trắng
a = 0
for i in files:
    gray = cv2.imread(i, 0)
    cv2.imwrite('C:/Users/bacht/Desktop/100k/1k-8/'+str(a) +".jpg", gray)
    a = a + 1

#cv2.imwrite() method is used to save an image to any storage device
#cv2.imwrite(filename, image)


