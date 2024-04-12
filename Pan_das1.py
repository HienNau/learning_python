import pandas as pd
#https://pandas.pydata.org/docs/reference/series.html
#https://blog.hocexcel.online/68-dong-code-python-hay-su-dung-xu-ly-du-lieu-trong-pandas.html
#https://freetuts.net/ket-hop-cac-tap-du-lieu-trong-pandas-3472.html
### Series
#Series là mảng một chiều giống như mảng Numpy, hay như một cột của một bảng (array numpy là 1 dòng), nhưng nó bao gồm thêm một bảng đánh label.
#Tao Series khong truyền index
s = pd.Series([0,1,2,3])
print(s)
print(s.shape[0])
s.index = pd.date_range('1999/1/31', periods=s.shape[0])
print(s)
#Tao Series có truyền index
e_list = [0,1,2,3]
print(pd.Series(e_list, index=["a","b","c","d"]))
#Tao Series từ Dict
data = {'a' : -1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
ex = pd.Series(data, index=["a","c","b","f","g"])
print(ex)
#Truy cập index:
print(ex["b"])
print(ex["a":"c"]) # Lấy luôn cả giá trị của "c"
print(ex[:3]) # Lấy như bình thường, lấy index 0,1,2, không lấy index 3
print(ex[3:])
print(ex[-3:]) # Lấy 3 dữ liệu cuối
print(ex[::-1])
print()
#Tạo Series từ Scalar 
print(pd.Series(5,index=[1,2,3,]))
# Lấy dạng array của Series bằng numpy.asarray
import numpy as np
print(np.asarray(ex))

### Data Frame:
# Một DataFrame là sự kết hợp của nhiều Series đóng vai trò như các cột
# Tạo DataFrame từ dict các Series
ex_dict = {"một": pd.Series([1,2,3,4],index=["a","b","c","e"]),
           "hai": pd.Series([1,2,3,5],index=["a","b","d","e"])}
print(ex_dict)
ex1 = pd.DataFrame(ex_dict)
print(ex1)
ex2 = pd.DataFrame(ex_dict,index=["a","b","c"])
print(ex2,end="\n"+"\n")
ex_d = {"một": pd.Series([1,2,3,4],index=["a","b","c","e"]),
           "hai": pd.Series([1,2,3,5],index=["a","b","d","e"]),
           "ba": pd. Series([7,8,9,0],index=["a","c","d","e"])}
ex = pd.DataFrame(ex_d)
print(ex["ba"]) # lấy dữ liệu của cột "ba", kq trả về 1 series
# Chèn thêm cột:
ex["bốn"]= ex["một"]-ex["hai"]
print(ex)
ex.insert(1,"năm",ex["một"]) #chèn ngay vị trí thứ 1
print(ex)
ex["sáu"] = "Hiền Nâu"
print(ex)
ex["bảy"] = 0
ex["tám"] = ex["ba"][ex["ba"]>8]
print(ex)
ex["chín"] = ex["một"][ex["một"]==2] # hoặc là: ex["chín"] = ex["một"] == 2
print(ex)
ex["mười"] = ex["bảy"][:"c"]
print(ex)
# Xóa cột bằng lệnh del hoặc pop:
del(ex["bảy"])
print(ex)
ex.pop("năm") # Không gán giá trị vẫn được
print(ex)
# Lấy các dòng dữ liệu:
print(ex.iloc[1]) # lấy theo chỉ mục
print(ex.loc["b":"d"]) # lấy theo tên # ex.loc(:,["ba","bốn"])
print(ex[1:3]) # slice 1 số dòng (lấy như bình thường, dòng 1 và dòng 2 được lấy ra), giống như lấy dòng bên numpy
print(ex[["một","ba"]]) # Truy cập tới nhiều cột bất kí bằng [[]], giống numpy
print(ex.iloc[1,1]) # Lấy dữ liệu ô, hoặc dùng .at, .iat # ex.iloc(:,1)
# Đổi tên các cột theo thứ tự:
ex.columns = ["một","hai","ba","bốn","năm","sáu","bảy","tám"] #Tương tự với index
print(ex)
ex.dropna(axis=1,thresh=3) #Cách bỏ các dòng có nhiều hơn n giá trị null
ex.fillna("H")
print(ex)
print(ex.bốn) # Cách khác thay vì để trong dấu ngoặc
print(ex.ba["c"])
newex = ex.rename_axis(columns={"bốn":"chín"}) #Chạy không ra kết quả
print(newex)
ex["năm"].replace("Hiền Nâu","Hien") #Chạy không ra kết quả
print(ex)
print(ex.iat[0,0])
print(ex.at["b","ba"])
print(ex[:3])
print(ex[1:3])
print(ex.index)
print(ex.columns)
print(ex.to_numpy()) # Đọc file bằng numpy không cần labels hàng và cột
print(ex.values) # Đọc file bằng numpy
ex.to_csv("Hiền Nâu") # Tạo file CSV
print(pd.read_csv("Hiền Nâu",index_col=0)) # Đọc file csv
import numpy as np
ex_edit = ex.astype(dtype={'ba': np.float32, 'bảy': np.float16})
print(ex_edit.dtypes)
print(ex.loc[["a","c","e"],["ba","sáu","tám"]])
print(ex.iloc[[0,2,4],[3,5,7]])
ex.iloc[1:3,0] = np.array([4,5]) # Sử dụng array hay list đều dc
print(ex)
print(ex.iloc[0::2,0::2]) # Dùng chỉ số để ghi tắt, có thể dùng các hàm khác cũng trả kết qủa tương tự
print(ex.iloc[slice(0,None,2),slice(0,None,2)])
print(ex.iloc[np.s_[0::2],np.s_[0::2]])
print(ex.iloc[pd.IndexSlice[0::2],pd.IndexSlice[0::2]]) # Không dùng np.index_exp[0::2] được vì nó sẽ trả về kết quả là (slice(0,None,2),)
print(ex.iloc[np.index_exp[0::2][0],np.index_exp[0::2][0]])
print([ex["ba"]>8])
new = ex.rename_axis("tám",axis = 1)
print(new)
new = ex.rename_axis("tám")
print(new)
