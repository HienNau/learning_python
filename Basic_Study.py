k= "Hien"
print (type(k))
from decimal import*
getcontext().prec = 20
t= Decimal(10)/3
print(t)
#https://tuhocict.com/iterable-iterator-trong-python/
t= (1,2,3)
print(t[2])
#######
from fractions import*
t = Fraction(6,9)
print(t)
print (type(t))
print(10%3)
print('''I'm "Hien Nau"''')
print("""I'm
Hien
Nâu""")
print('\a')
print('I\'m Hien Nau')
print(r"Hien Nau\n")
print("Hien"+"\n"+"Nau")
print("H"*3)
x= "Hien"
y="H"
print(y in x)
Str = "Hien Nau"
#Str[2]="E" => Đ/v chuỗi không thay đổi phần tử của chuỗi dc như List. Mà phải dùng hàm replace như ở dưới
print(Str) # => Đ/v chuỗi không thay đổi phần tử của chuỗi dc như List
print (Str[0])
print(Str[len(Str)-1]) #Cùng kq với print(Str[-1])
print(Str[0:4])
print(Str[:]) #None:None
i= float(8.9)
print(i)
j= str(8)
k= str(9)
print(j+"\n"+k)
ex= "NguyenThiThuHien"
print(ex[None:11:-1])

print(int("6"))
ex= "MinhKhoiooo"
print(ex[None:6]+"0"+ex[7:None])
print("MinhKhoi".replace("o","0",3)) #=> Thay đổi nội dung của chuỗi
print("NguyenThiThu%s" %("Hien"))
print("NguyenThiThu%r" %("Hien"))
k= "N %s H %s"
print(k)
print(k %("-","#"))
print("%.20f" %(10/3)) # Giống hàm Decimal # Hàm dùng cho số thực
print(f'a\tb')
z="Hien"
print (f'{z} Nau')
name ="Hien"
sdt ="035"
phone="3470802"
print(f'Name:{name}\nSDT:{sdt}\nPhone:{phone}')
print("\\t")
print(f'Name:{{name}}\nSDT:{sdt}\nPhone:{phone}')
print("a=%d,b=%d,c=%d" %(1.9,2,3)) # Lấy phần nguyên
print("a={},b={},c={}".format(1,2,3)) # Giống hàm f' string nhưng gọn hơn
print("a={2},b={0},c={0}".format("a","b","c"))
print("a={Vo},b={chong},c={con}".format(Vo= "H", con = "K",chong ="Hung"))
r="a={Vo},b={chong},c={con}".format(Vo= "H", con = "K",chong ="Hung")
print(r)
print("{:^5}".format("k")) # căn lề
a= "Nguyen ThiThu Hien"
print("{:<6} - {:^6} - {:^6} - {:>6}".format("Nguyen","Thi","Thu","Hien"))
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.swapcase())#Chữ hoa thành chữ thường và ngược lại
print(a.title()) 
print(a.center(60,"-"))
print(a.rjust(60,"-"))
print(a.ljust(60,"-"))
print(a.join(["-","*","~"]))
t= "*NguyenThiThuHien**"
print(len(t))
print(t.strip("*")) #lstrip, rstrip
print(a.split(" "))
print(a.split(" ",1))
print(a.partition("t")) #ki tư khong xuat hien trong chuoi thì se tra ve khoang trang
print(a.count("i",5,15))
print(a.startswith("T",7,12))
print(a.endswith("n"))
print(a.find("T",8)) #Giống hàm Instr trong VBA
print(a.index("T",8))#Giống hàm find nhưng ko tìm thấy thì báo lỗi thay vì trả kq là -1
print(a.isdigit())
print(a.isspace())
a=[i for i in range (20)]
print(a)
r= [[n*5,n*10] for n in range(1,4)]
print(r)
k= list("1111") #P.Thức interable (chuỗi, list) # Tạo constructor
print(k)
k=[1,2]
k+=[["a","b"],"c"] #Giống với k.__add__([["a","b"],"c"])
print(k)
k*=1 # Nhân chuỗi lên 1 cơ số lần
print(k)
print("c" in k) # đối với chuỗi thì sd hàm find để tìm thứ tự, nếu kq -1 là không xuất hiện. Hoặc dùng hàm count để tìm số lền xuất hiện
print (k[2][1])
print(k[0:None]) #Hoặc [0:]
print(k[0:3])
print(k[::-1]) #Lấy toàn bộ và đảo ngược
k[2]="t" #Thay đổi nội dung của list
print(k)
#Ma trận
a=[[1,2,3],[4,5,6]]
print(a[0])
print(a[1])
print(len(k))
print(k.count("c"))
print(k.index("c"))
print(k.__add__([["a","b"],"c"]))
x= "Go"
if x== "Go":
	print("Go ")
print("Mike")
a= 1
def do(x):
	return (a + x)
print(do(1))
k = "NguyenThiThuHien"
print(k[::2]) 
print(7//2)
l = [2,3]
print(5*l)
print("1"+"1")