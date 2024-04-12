#https://v1study.com/python-tham-khao-pandas-dataframe-lam-viec-voi-du-lieu-mot-cach-thu-vi.html
import pandas as pd
import numpy as np
da_ta = {"name":["Hiền","Hùng","Minh Khôi","Hạnh Mon"],"Tỉnh/TP":["An Giang","Phú Yên","HCM","AG"],"Score":[9,8,10,7],"Age":[30,35,4,29]}
Data_T = pd.DataFrame(data=da_ta,index=np.arange(4),columns=["name","Tỉnh/TP","Age","Score"])
Data_T.rename(columns={"Age":"Tuổi"}) #Code không chạy
print(Data_T)
Job = pd.Series(["Nội trợ","IT","Mầm 1","Banker"]) #, index= Data_T.columns,name="JOB"
Data_T.insert(4,"Job",Job) # Insert cột
Add = pd.Series(["Bé","HCM","1","10","Child"], index= Data_T.columns,name=4)
Data_T = Data_T.append(Add) # append dòng
print(Data_T)
Data_T = Data_T.drop(labels = 4) # Hoặc để 4

Data_T["Extra"] = [1,2,3,4]
print(Data_T)
Data_T = Data_T.drop("Extra",axis = 1) # Hoặc dùng các câu lệnh phía dưới. Nếu không có đối số axis = 1 thì giống câu lệnh xóa dòng
#S= Data_T.pop("Extra")
#print(S)
print(Data_T)
Data_T.insert(5,"Total", value = Data_T["Age"]+ Data_T["Score"]) # Hoặc dùng câu lệnh bên dưới
# Data_T["Total"] = Data_T.Age + Data_T.Score
print(Data_T)
avg = Data_T.loc[:,["Score","Total"]] # Phải có .loc
Data_T.insert(6,"AVG",np.average(avg,axis = 1, weights = [0.5,0.5]))
# Hoặc là : Data_T["AVG"] = np.average(avg,axis = 1, weights = [0.5,0.5])
print(Data_T)
T=Data_T.sort_index(axis = 1,ascending= False) # Sắp xếp theo nhãn, thay đổi axis để đổi trục
Sorted = Data_T.sort_values(by = 'Total' , ascending = False) #by=["AVG","Score"],ascending =[False,False]
print(Sorted)
print(Data_T[Data_T["Score"]>=8]) # Lấy những dòng tương ứng với GT True, Fale không lấy
print(Data_T[(Data_T["Score"]>8) | (Data_T["Total"]==36)]) # Kết hợp điều kiện (|,&,^,~)
print(Data_T["Total"].where(Data_T["Total"] > 35, other = "Rớt"))
print(Data_T.describe())
for col_label, col in Data_T.items():
    print(col_label, col, end= "\n")
for col_label, col in Data_T.iteritems():
    print(col_label, col, end= "\n")
for row_label, row in Data_T.iterrows():
    print(row_label, row)
for row in Data_T.iloc[:,[2,3,4]].itertuples(name = Data_T.loc[0,"name"],index=  True): #Thêm tham số (name = "Tup",index=  False) để đặt tên và ko xem tên hàng
    print(row)
rangeDT = pd.date_range(start= "2023-03-25", periods= 5, freq= "Min")
print(rangeDT)
DT = pd.DataFrame(np.arange(5), index= rangeDT)
print(DT)
ex_range = DT.resample(rule = "2min")
print(ex_range)
print(Data_T)
Sorted = Data_T.sort_values(by = ["Total","AVG"] , ascending = [False,True]) #by=["AVG","Score"],ascending =[False,False] # Phải bỏ axis đi thì chạy mới đúng
print(Sorted)