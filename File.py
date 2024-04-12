print(open("Untitled-1.py", mode =("r")))
file = open("Untitled-1.py", mode =("r"))
print(file.read(4))
print(file.readline(7)) # => Kết quả trả về giống read(7)
print(file.readline()) #ĐỌc từng dòng
print(file.read())#đọc đến hết file
file.close() # => Đưa con trỏ về đầu dòng
file = open("Untitled-1.py", mode =("r"))
print(file.readlines()) #Trả kết quả giống list(file)
file = open("Untitled-1.py", mode =("r"))
data = list(file) #=> Vì data nhận kết quả từ hàm open là  interable nên có thể dùng constructor list, các constructor này cũng đưa con trỏ về cuối file
print(data)
file = open("Untitled-1.py", mode =("r"))
data = tuple(file) 
print(data)
file = open("Untitled-1.py", mode =("a+"))
data=file.write("\nHienNau") # Trả về số kí tự dc ghi vào
print(data)
file = open("Untitled-1.py", mode =("r"))
data1 = file.readline()
file.seek(0)
data2=file.readline()
print(data1)
print(data2)
H_f=open("H-f.py","w+")
H_w=H_f.write("HienNau\n")
H_f.seek(0)
print(H_f.read()) #Không đọc file đc do write xong con trỏ đang ở cuối file => Dùng hàm seek(0) để đưa con trỏ về đầu file
#Câu lệnh with: https://howkteam.vn/course/lap-trinh-python-co-ban/xu-ly-file-trong-python-1570