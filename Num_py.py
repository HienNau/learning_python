import pandas as pd
import numpy as np
s = pd.Series(["a", "b", "c"], name="vals")
s = s.to_frame()
print(type(s))
print(np.random.seed(10))
data = np.random.normal(100, 20, 200)
print(data)

my_list = [[1,2,3],[4,5,6],[7,8,9]] #tạo mảng 2 chiều
print(np.array(my_list))

a = np.arange(6)
print(a)
b= np.arange(0,11,2)
print(b)

print (np.zeros(3))
print(np.ones((3,3),dtype=int)) #bỏ vào 2 dấu ngoặc

print(np.linspace(0,10,11)) # Công thức: (10-0)/(11-1) #
print(np.linspace(0,15,6))

print (np.eye(3)) # Ma trận indetity, ma trận vuông, đường chéo chính bằng 1

print (np.full((3,3),1))

print(np.random.rand(2)) # Phân phối đồng nhất trong khoảng 0-1
print(np.random.rand(2,3))

print(np.random.randn(2))  # Phân phối chuẩn hình chuông
print (np.random.randn(2,3)) 

print (np.random.randint(0,10)) # Trả về mảng là 1 số nguyên từ nhỏ (bao gồm) đến lớn (không bao gồm)
print (np.random.randint(0,10,3))

ex = np.arange(25)
print(type(ex))
print (ex.reshape(5,5).ndim)
print (ex.dtype)
print(ex.shape)
print(ex.size)

print(ex.reshape(1,25).shape)
print(ex.reshape(25,1).shape)
print (ex.reshape(5,5))
print(ex.max())
print(ex.argmax())
print(ex.min())
print(ex.argmin())
print(ex.reshape(5,5)[[1,2,3,4]]) # Truy cập tới nhiều dòng bất kí bằng [[]]

print(ex[ex > 20])

#Đọc mảng từ file txt:
    #diem_2a = np.loadtxt('Diem_2A.txt', dtype = int, delimiter=',') #ở đây tất cả phần tử là số nguyên nên mình để kiểu int cho dễ nhìn, các phần tử phân tách nhau bởi dấu ","

    #print("File dữ liệu điểm lớp 2A:\n", diem_2a)

# https://pythonnangcao.com/khoa-hoc/bai-3-toan-tu-trong-numpy-numpy-operations/
