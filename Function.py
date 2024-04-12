def Hien(text, age):
	print(text,age)
Hien("Hien Nau",30)
def Hello(name):
	print("Hi",name + "!") 
Hello("Hien")
Hello("Hung")
def Hello(name, greating = "Hi"):
	print(greating,name + "!") 
Hello("Hien","Chao")
Say = "Sayhello"
def Hello(name, greating = Say):
	print(greating,name + "!") 
Hello("Hien","Hello")
Hello("Hien")
def k(arr = []):
	arr.append("F")
	print(arr)
k(["H"])
k()
k()
help(sorted)
print(sorted((3,2,5),key=None, reverse = False))
tup =(1,2,3)
def H(a,b,c,*,d=4):
	print(a,c)
	print(b,d)
H(*tup,d=5)
def H(*args): #*args thay cho lệnh tuple()
	print(args)
	print(type(args))
H(*(i for i in range (3)))
def ex(*args, H="HienNau"):
	print(args)
	print(type(args))
	print(H)
ex((93,18,11),"Thuhien","Hien",H="HN")
dic= {"Ten":"Hien","Tuoi":30}
print(type(dic))
def H(Ten,Tuoi): # Tên biến phải trùng với tên Key
	print(Ten,Tuoi)
H(**dic)
def H(H,**kwargs): #**kwargs thay cho lệnh dict(Ten = "Hien",Tuoi = 30)
	for k,v in kwargs.items():
		print(k,"=>",v)
	print(H)
	print(kwargs)
H("Hien",Ten = "Hien",Tuoi = 30)
l= ["Hien","Hung","MinhKhoi"]
def H(arg):
	arg[0]="HienNau"
	print("Everything is changed")
print(l)
H(l)
print(l)
def EX():
	global x
	x = 1
def ex():
	x =0
	print("localargs la:",x)
EX()
print(x)
ex()
print(x)
dai = 4
rong = 5
def CV(d,r):
	Chuvi= (d+r)*2
	return Chuvi
KQ = CV(dai,rong) # Tạo biến để hứng đồng nghĩa với việc đã gọi hàm (thêm hàm print để kiểm chứng)
print(KQ)
CV(3,2) # Gọi hàm nhưng không trả kết quả
print(CV(3,2)) # => Kết quả dc hàm print hứng
def Vidu ():
	print("Đã dừng")
	return
	print("Khong dc hien thi")
none = Vidu() #gặp return thì hàm sẽ dừng
Vo,Chong,Con = "Hien","Hung","Minhkhoi"
print (Con)
Vo,Chong,Con = ["Hien","Hung","Minhkhoi"] # ở đây, cũng có thể sử dụng list hoặc một container bất kì
print(Chong)
def HinhChuNhat (dai, rong):
	Chuvi = (dai+rong)*2
	Dientich = dai * rong
	return Chuvi,Dientich # Không liên quan với tên biến được tạo để hứng kết quả
CV,DT= HinhChuNhat (5, 3)
print(CV,DT)
#GIAI BAITAP CUNG CO
y = x**3 + 2*x**2 - 4*x +1
l =[(-5,-20),(-4,-15),(-3,4),(-2,9),(-1,7),(0,1),(1,-7),(2,-9),(4,81),(5,130)]
#Cách 1:
A=[]
sumA=0
sumB= 0
B=[]
for i in l:
	if i[1]== i[0]**3 + 2*i[0]**2 - 4*i[0] +1:
		A.append(i)
		sumA+=i[1]
		continue # Hoặc dùng else	 
	B.append(i)
	sumB+=i[1]
print(A)
print(sumA)
print(B)
print(sumB)
print(abs(sumA-sumB))
# Cách 2:
def f(x):
	return x**3 + 2*x**2 - 4*x +1
def check(x, y):
    if y == f(x): # Kiểm tra 1 mđ nên không cần dùng else
        return True
    return False
def add_list(lt):
	A =[]
	B=[]
	for i_list in lt:
		if check(*i_list):
			A.append(i_list)
			continue
		B.append(i_list)
	return A,B
def sum_y(l_point):
	sum_y= 0
	for y_point in l_point:
		sum_y+= y_point[1]
	return sum_y
listA, listB= add_list(l)
print(listA)
print(listB)
#sum_A = sum_y(listA)
print(sum_y(listA)) #Khỏi dùng biến hứng giá trị
sum_B = sum_y(listB)
print(sumB)
print (abs(sum_y(listA)-sum_y(listB))) #Tính trc rồi in sau
a=32
b=59
c=8
d=24
e=15
def so_sanh(x,y):
	if x> y:
		return x
	return y
max_num = so_sanh(a,so_sanh(b,so_sanh(c,so_sanh(d,e)))) # Số lớn nhất trong  số a,b là: (a+b + abs(a-b))/2
print(max_num*2-1)
H = (i for i in range (3))
print(H)
print(type(H))
for i in H: # chỉ in 1 lần, không in lại lần 2 được
	print (i)
def square(l):
	square_l =[]
	for i in l:
		square_l.append(i**2)
	return square_l
l= [1,2,3]
square_l = square(l)
print(square_l)
def square_y(l):
	for i in l:
		print(i)
		yield i**2
#print(square_l_y) # Trả về 1 gen
for i in square_y(l):
	print(i)
def test():
	yield "Hien"
	print("Thứ 1")
	yield "Hung"
	print("Thứ 2")
	yield "Minh Khôi"
	print("Cuối cùng")
for i in test():
	print (i)
	print("Next")
def gen ():
	for i in range(4):
		x= yield i
		print("Hien Nau",i) #Thực hiện hết dòng lệnh for
for k in gen():
	print(k)
#Chỗ này không hiểu: 
def gen ():
	for i in range(8):
		x= yield i
		print("Ten",x)
gen = gen()
next(gen)
gen.send("Hien")
next(gen)
gen.send("Hung")
next(gen)
gen.send("H")
next(gen)
gen.send("Minhkhoi")
ave =lambda a,b,c =6: (a+b+c)/3 # => Lambda là 1 expression
print(ave(1,2,9))
def test():
	name = lambda x: print(x + " là tên của tôi")
	return name # return lưu trữ hàm nặc danh
kq = test() # kq = name lúc này là một hàm nặc danh
kq ("HienNau") # Bỏ print ở trên thì phải ghi print(kq ("HienNau"))
print(kq) #Giống như lệnh type
vd_list = [lambda x : x*2, lambda x: x*3, lambda x: x*4]
vd_l=[]
for i in vd_list:
	#print(type(i)) # => function
	vd_l.append(i(2))
	print(i(2))
print(vd_l)
print(vd_list[0](2))
D= {"Họ": lambda: "Nguyễn","Tên":lambda: "Hien","Tuoi":lambda: 30} # argument để trống nhưng bắt buộc phải có expression
i= "Tuoi"
print(D[i]()) #Thêm dấu () để gọi lambda thì mới xuất gt 30
#Thay vì dùng lambda thì dùng def sẽ như thế này:
def f1(): return 'Goooooooog'
def f2(): return 'Youuuuuuuuu'
def f3(): return 'Free Education'
key = 'Kteam'
print({'Google': f1, 'YouTube': f2, 'Kteam': f3}[key]()) #Thêm () để chạy hàm
so_sanh = lambda x,y: x if x>=y else y
print(so_sanh(1,2))
kiemtra = lambda x: "chia het" if x% 3 ==0 else "không chia het"
print(kiemtra(8))
kiemtra = lambda x: "khong chia het" if not (x% 3==0) else "chia het"
print(kiemtra(9))
def sub_name(ten):
	nhap_ten = lambda main_name: "Tên ở nhà là: " + main_name
	return nhap_ten
print(sub_name("Hien")("Hiêm"))
inc = lambda x: x + 1
kteam = [1, 2, 3, 4]
print(map(inc,kteam))
print(list(map(inc,kteam)))
inc = lambda x: x + 1
kteam = [1, 2, 3, 4]
print([inc(x) for x in kteam]) # List comprehension
a = [3,4,5]
b = [7,8,9]
print (list(map(pow,a,b)))
#print([pow(i,j)for i,j in a,b]) #Không dùng comprehension được
list_vd = [1, -3, 5, 0, 2, 6, -4, -9]
print([x for x in list_vd if x < 0])
ex_list =[None, 0 ,"",-2,1,9]
print(list(filter(None, ex_list)))
from functools import reduce
list_vd=[32,59,8,24,15]
so_sanh = lambda x,y: x if x>y else y
print(reduce(so_sanh,list_vd))
ex= [2,3,4,5]
func = lambda x,y: x+y # Khác với hàm map có 2 argumemt
print(reduce(func,ex))
#Chỗ này không hiểu
def cal_sum(lst):
	idx0, *r = lst # idx0, r = lst[0], lst[1:]
	return idx0 if not r else idx0 + cal_sum(r)
print(cal_sum([1,2]))
#Dãy Fibonaci dùng vòng lập:
lst=[i for i in range(20)]
print(lst)
list_kq= []
def Fibonaci(lst):
	idx = 0
	while idx < len(lst) -1 :
		list_kq.append(lst[idx]+lst[idx+1])
		idx = idx +1
	print(list_kq)
Fibonaci(lst)
#Dãy Fibonaci dùng đệ quy:
lst = [x for x in range(5)]
list_kq =[]
def Fibonaci(lst):
	if len(lst)==1:
		return list_kq.append(lst[0])
	else: 
		while  len(lst)>1:
			list_kq.append(lst[0]+lst[1])
			lst = lst[1:]
print(list_kq)
#Fibonaci(lst)




