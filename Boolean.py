print(5*0 != 0)
print("Hien"=="hien")
print("Hien"=="Hien")
print(ord("H"))
H=[1,2]
h=[1,2]
#h=H
print(H==h) # So sánh bằng giá trị
print(H is h) #so sánh bằng id, H là H còn h là h
a= -4
b= -4
print(a is b) #Các số từ -5 đến 256 và một số chuỗi có số kí tư dưới 20 sẽ trả về cùng id
print(bool(0)) # Só 0 None và "" trả về kết quản bool là false, còn lại trả về True
print(bool(None))
print(bool(""))
print(int(True))
print(int(False))
print(int(8.9))
n=2
print(n in (1,3,4)) #Kiểm tra 1 số có bằng các số kia không