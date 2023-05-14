####Bài tập Python level 1
#Bài 1:
kq=[]
for x in range (2000,3201):
	if x%7 == 0 and x%5 != 0:
		kq.append(str(x))
#for i in kq:
##	print(str(i)+",", end =" ")
print(", ".join(kq))
#Bài 2
#x= int(input("So can tinh giai thua:"))
def Giai_Thua (x):
	if x==0:
		return 1
	else:
		return x*Giai_Thua(x-1)
print(Giai_Thua(7))
#Bài 3:
Dict= {}
def Tao_Dict(n):
	for i in range (1,n+1):
		#return Dict.update(i=i*i)  => Câu lệnh này là Sai 
		#Dict[i]= i*i =>Dùng này cũng đúng
		#Dict.update(i=i*i) => Không dùng update mà phải là Dict[i], dùng update thay đổi phần tử của dict
		Dict.setdefault(i,i*i)
	return Dict
print(Tao_Dict(5))
#Bài 4:
s = "34,67,55,33,12,98"
#s=  input("Nhap chuoi so:")
print(s.split(","))
print(tuple(s.split(",")))
# Bài 5:
#class Str:
#	def __init__(self):
#		self.Str = ""
#	def getString(seft):
#		seft.Str = input("Hay nhap chuoi:")
#	def printString(seft):
#		print(seft.Str.upper())
#Nhap_Str = Str()
#Nhap_Str.getString()
#Nhap_Str.printString()
#Tự VD:
class NhanVien:
	def __init__(self,name,age,GT):
		self.name = name
		self.age = age
		self.GT = GT
	def infor(self):
		print(self.name,self.age,self.GT)
ly_lich = NhanVien("Hien",30,"female")
ly_lich.infor()
# Bài 6:
def square(n):
	return pow(n,2)
print(square(5))
#Bài 7:
def square(n):
	'''Trả lại giá trị bình phương của số được nhập vào.
	Số nhập vào phải là số nguyên.
	return pow(n,2)'''
print(square.__doc__)
# Bài 10:
hours = 50
#hours = float(input("Tong so gio lam cua nhan vien: "))
salary = 20
#salary = float(input("Thu lao tren moi gio lam: "))
luong = lambda x: x*20 if x <= 44 else 44*20 + (x-44)*2*1.5
print("luong thuc lanh cua nhan vien là:",luong(60),"nghìn đồng")
####Bài tập Python level 2
#Bài 1:
from math import *
C = 50
H = 30
D_input= "100,150,180"
D= D_input.split(",") #Trả về list D
# 2 câu lệnh rút gọn thành: D= [x for x in input("Nhap cac gt cua D: ").split(",")]
list_kq = []
def Tinh_Q(D):
	for i in D:
		Q = sqrt((2 * C * int(i))/H)
		list_kq.append(str(int(round(Q))))
	return list_kq
print(",".join(Tinh_Q(D)))
# Bài 2:
arr=[]
i = 3
j = 3
for i in range(i+1):
	arr.append([])
	for j in range(j+1):
		arr[i].append(i*j)
print(arr)
#Bài đáp án:
dimensions =[4,4]
# dimensions = [int(x) for x in input("Nhap x,y: ").split(",")]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)] #[0,0,0,0]
# print(multilist) => Trả về  list với toàn bộ phần tử bằng 0
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col # Thay đổi giá trị của phần tử trong list
print (multilist)
# Bài 3:
string = "without,hello,bag,world"
#string = input("Vui long nhap chuoi: ")
print(",".join(sorted(string.split(","))))
# Bài 4:
string= "Hello world\nPractice makes perfect"
#string = input("Nhap chuoi: ")
print(string.upper())
# Bài 5:
string = "hello world and practice makes perfect and hello world again"
#string = input("Nhap chuoi: ")
set_output = sorted(set(string.split(" "))) # Hàm sorted trả kết quả là 1 list
print(" ".join(set_output))
# Bài 6: 
string ="0100,0011,1010,1001"
# string = input("Nhap chuoi nhi phan: ")
list_num = [int(x,2) for x in string.split(",")]
print(list_num)
list_kq = []
for i in list_num:
	if not i%5:
		list_kq.append(str(i))
print(",".join(list_kq))
# Bài 7:
list_kq =[]
for n in range(2000,3001):
	i= str(n)
	if  (int(i[0])%2 ==0) and (int(i[1])%2==0) and (int(i[2])%2==0) and (int(i[3])%2==0):
		list_kq.append(i)
print(",".join(list_kq))
# Bài 8:
string = "hello world! 123"
kq ={"sum_chucai":0,"sum_chuso":0}
#sum_chucai = 0
#sum_chuso = 0
for i in string:
	if i.isdigit():
		kq["sum_chuso"]+=1
	elif i.isalpha():
		kq["sum_chucai"]+=1
print("So chu so trong chuoi la:",kq["sum_chuso"],"\n"+"So chu cai trong chuoi la:",kq["sum_chucai"])
#Bài 9:
string = "Quản Trị Mạng"
kq= {"So chu hoa":0,"So chu thuong":0}
for i in string:
	if i.isupper():
		kq["So chu hoa"]+=1
	elif i.islower():
		kq["So chu thuong"]+=1
print("So chu hoa trong chuoi la:",kq["So chu hoa"],"\n"+"So chu thuong trong chuoi la:",kq["So chu thuong"])
#Ví dụ trên FB: Tính tổng S = 1/(1*2*3)+1/(2*3*4)+...+1/(98*99*100)
S_List = [(x-2)*(x-1)*x for x in range(3,101)]
Sum_S = 0
for i_list in S_List:
	Sum_S += 1/i_list
print (Sum_S)
# Ví dụ nhập 1 số trong hệ thập phân bất kì, xuất ra màn hình bằng chữ của chữ số đó
#x = input("Hãy nhập số: ")
x= "99"
i = int(x[0])
F_List= ["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
print(F_List[i])
#Ví dụ trên FB:
dict_diem ={":))":4, ":)":2,":((":-5,":(":-1}
string_emotion = ":)).:(.:).:((.:)"
list_emotion = string_emotion.split(".")
def score_emotion (list_emotion):
	score_emotion = int()
	for x in list_emotion:
		score_emotion +=  dict_diem[x]
	return score_emotion
print(score_emotion(list_emotion))




