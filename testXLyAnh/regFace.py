from google.colab import drive
drive.mount('/content/drive')
from PIL import Image
import numpy as np
import glob
from numpy import linalg

image=[]
queue_list = []
image_vector =[]
#############################################################
# BƯỚC 1: THU THẬP ẢNH MẶT NGƯỜI, KÍCH THƯỚC 128x128

# đọc file ảnh từ thư mục stock ảnh
for filename in glob.glob('/content/drive/My Drive/stock/image-1k/*.jpg'):
    im=Image.open(filename)
    queue_list.append(im)   
    im= np.asarray(im,dtype=float)
    image.append(im)
# chuyển file ảnh về dạng vector 16k chiều
for i in range(len(image)):
    p=image[i].flatten()
    image_vector.append(p)

###############################################################
# BƯỚC 2: TÍNH MA TRẬN D, MỖI DÒNG LÀ 1 VECTOR 16K CHIỀU

# tính ma trận D
matrix_D = np.matrix(image_vector)
# vector_mean của D
mean= matrix_D.mean(0)


###############################################################
# BƯỚC 3: TÍNH MA TRẬN U BẰNG CÁCH DỊCH GỐC VỀ MEAN CỦA D

column =0
matrix_U= np.ones((len(image),16384))
for values in image_vector:
    zm= matrix_D[column] - mean
    matrix_U[column] =zm
    column = column +1

###############################################################
# BƯỚC 4: TÍNH MA TRẬN HIỆP BIẾN:

# ma trận hiệp biến của ma trận U kích thước n x n
d = (np.dot(np.transpose(matrix_U),matrix_D))/(len(image)-1)

# Tính  eigenvector và eigenvalue
# w2: vector riêng 1x16k ; v2: trị riêng 16kx16k
w2, v2 = linalg.eigh(d)
print("vector rieng: ", w2)
print("tri rieng: ", v2)

###############################################################
# BƯỚC 5: THÀNH LẬP MA TRẬN GỒM CÁC VECTOR RIÊNG CỦA MA TRẬN HIỆP BIẾN

# không gian PCA
  # Lấy 20 vector riêng ứng với 20 trị riêng lớn nhất
list_index = [] # lưu giá trị các cột chứa vector riêng tương ứng với trị riêng lớn nhất 
max_list = w2.max()
min_list = w2.min()
for i in range(16384):
    if w2[i] == max_list:
        list_index.append(i)
for k in range(19):
    for i in range(16384): 
        if w2[i] < max_list and w2[i] >= min_list:
            min_list = w2[i]
    for i in range(16384):
        if w2[i] == min_list:
            list_index.append(i)
    max_list = min_list
    min_list = w2.min()
list_index.reverse()

# ma trận chứa 20 vector riêng ứng với trị riêng lớn nhất (nxm)
matrix_P= np.ones((16384,20))
for i in range(16384):
    for j in range(20):
        matrix_P[i,j] = v2[i,list_index[j]]
print("ma tran chua 20 vector rieng: \n", matrix_P)

#######################################################################
# BƯỚC 7: Chiếu từng vector sang không gian PCA và lưu vào csdl: facialRecognation.npy
list_vector_pca = []
for i in range(len(image_vector)):
    pca = np.dot(image_vector[i],matrix_P)
    list_vector_pca.append(pca)
np.save('/content/drive/My Drive/stock/facialRecognation.npy',list_vector_pca)


#################################################################################
# BƯỚC 8: VỚI 1 ẢNH MỚI ĐẦU VÀO: CHIẾU SÁNG PCA; SO SÁNH CÁC VECTOR TRONG CSDL -> ĐƯA RA KẾT LUẬN

list_vector_pca = np.load('/content/drive/My Drive/stock/facialRecognation.npy')# list các vector trong không gian pca 

image_test = '/content/drive/My Drive/stock/image-1k/474.jpg' # ảnh test 
img_test = Image.open(image_test)
vector_image = np.asarray(img_test,dtype=float).flatten()
vector_pca_test = np.dot(vector_image,matrix_P)

# Tính toáng khoảng cách o-clid
# giữa vector test với các vector trong không gian pca
list_dist = []
for vector in list_vector_pca:
    dist = np.linalg.norm(vector_pca_test - vector)
    list_dist.append(dist)
# Lấy ra 5 ảnh giống nhất
image_result = [] # lưu các ảnh kết quả thu được
for i in range(len(list_dist)):
    if list_dist[i] == min(list_dist):
        image_result.append(i)
min_list = min(list_dist)
max_list = max(list_dist)
if len(image_result) >= 5:
    print(image_result)
else:
    for k in range(5 - len(image_result)): 
          for i in range(len(list_dist)):
              if list_dist[i] > min_list and list_dist[i] <= max_list:
                  max_list = list_dist[i]
      
          min_list = max_list
          max_list = max(list_dist)
          for i in range(len(list_dist)):
              if list_dist[i] == min_list:
                  image_result.append(i)
    print("thu tu cua 5 anh giong voi anh dau vao nhat: ", image_result)

# Kết luận: Lưu lại file kết quả test
from PIL import Image
count = 0
for i in image_result:
    test_image = queue_list[i].save('/content/drive/My Drive/stock/test result/' + str(count) + '.png')
    count += 1