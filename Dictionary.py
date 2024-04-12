D= {k: v for k, v in [("Ten","Hien"),("Ns","1993")]}
print(D)
print(type(D))
D= {("Ten","ns"),("Hien","1993")} #Kiểu dữ liệu set
print(D)
print(type(D))
D=dict()
print(D)
print(type(D))
i=[("name","Hien"),("ns",1993)]
D=dict(i)
print(D)
D= {"Ten":"Hien","Ns":"1993"}
print(D["Ns"]) #=> Giống phương thức get phía dưới
print(type(D))
Ten="Hien" #=>Chỉ là trùng tên, không ảnh hưởng
Ns=1993 #=>Chỉ là trùng tên, không ảnh hưởng
D= dict(Ten="Hien",Ns="1993")
print(D)
print(type(D))
i= ("name","ns")
D= dict.fromkeys(i,"HienNau")
print(D)
print(dict.fromkeys(i,"HienNau"))
print(D["name"])
D["name"]="N"
print(D)
D["GT"]="Nu"
print(D) #=> Thêm cặp key-value mới
D= dict(Ten="Hien",Ns="1993")
D["Ten"]=D["Ten"]+"Nau"
print(D)
D["Ten"]+="Nau"
print(D)
D={"Ten": "Hien",(1,2):9}
d=D.copy()
print(d)
#print(D.clear())
#print(d.clear())
V=D.get("Ten")
print(V)
print(D.get("Ten")) # => Giống D["Ten"]
print(D.get("T","ThuHien")) 
print(D)
print(D.items()) 
print(type(D.items())) 
#i=[('Ten', 'Hien'), ((1, 2), 9)] #copy từ kết quả đem lên
i= list(D.items())
print(i)
print(dict(i)) # => Ngược lại của tạo dict
print(i[0])
print(i[0][0]) # Phải chuyển về list thì mới dùng indexing dc
D={"Ten": "Hien",(1,2):9}
print(list(D.keys()))
print(list(D.values()))
p=D.pop("Ten")
print(p)
print(D)
p=D.pop("Lop","CK")
print(p)
print(D)
D={"Ten": "Hien",(1,2):9}
pi=D.popitem() # => Lấy ra cặp key-value bất kì
print(pi)
print(D)
D={"Ten": "Hien",(1,2):9}
sd= D.setdefault("Ten")
print(sd)
sd= D.setdefault("Ho","Nguyen")
sd= D.setdefault("Tuoi",30) #=> Giống hàm get, khác ở chỗ có thêm phần tử vào dict =>Giống hệt hàm D[ho]
print(sd)
print(D)
D={"Ten": "Hien",(1,2):9}
D.update(Ho="Nguyen",Tuoi=29) #=> Ghi câu lệnh giống Constructor dict
print(D)
D={"Ten": "Hien",(1,2):9}
ud=D.update(Ten="HienNau")
print(D)
a={1:2,3:4}
b={1:2,6:7}
# print(a | b)
#Công dụng: Trả về một dict mới với các cặp key – value có mặt ở một trong 2 dict. Nếu một key bất kì có trong cả 2 dict, thì giá trị được lấy sẽ là cặp key – value ở Dict_B
acl=a.clear()
print(a)
print(acl)
d = {}
d.update({'a': 3})
d.update({'b': 9})
print(d)
d = {}
d.update(a=3)
print(d)
D= dict(Ten="Hien",Ns="1993")
D["Ten"]=D["Ten"]+"Nau"
print(D)
D["Ten"]+="Nau"
print(D)