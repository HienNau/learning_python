it=(x for x in range (3))
i= 0
while i< 6:
	try:
		print(next(it))
	except StopIteration:
		break
	i+=1
it=(x for x in range (3))
i= 0
while i< 3:
	print(next(it))
	i+=1

it=(x for x in range (3))
for i in it:
	print("Phan tu:",i)

it=[[1,2,3],9,0]
for i in it:
	print(i)
d = {"Ten":"Hien","Tuoi":30}
for k, v in d.items():
	if k == "Tuoi":
		break
	print(k,":",v)
st = "Hien Nau"
for s in st:
	if s ==" ":
		continue
	else: 
		print (s)
string = "Le Ngoc Hung."
for s in string:
	if s == ".":
		break
	print(s)
else: print("Da het chuoi")
setvd ={5,8,1,9,4}
Sum = 0
for n in setvd:
	Sum+= n
print(Sum)
setvd ={5,8,1,9,4}
print(type(setvd))
print(sum(setvd))
range(3,9)
print(range(3,9)[0])
print(list(range(3,9)))
r= range(8,0,-2)
print(list(r))
print(0 in r)
lt=[[2,1],{1,5,6},"33","Hien"]
print(type(lt))
for i in range(len(lt)):
	print(lt[i])
	for j in lt[i]: #Không dùng indexing cho set => CHuyển về câu lệnh for - in (không dùng range)
		print(j)
lt=[[2,1],(1,5,6),"33","Hien"]
i=0
while i< len(lt):
	print (lt[i])
	i+=1
lt = [1,2,3]
for i in range(len(lt)):
	lt[i]+=1
print(lt)
# sequence scan => tham trị : copy ra để dùng
# indexing scan => tham chiếu >>> https://www.youtube.com/watch?v=LwC0n2A6QRQ&t=1366s : Dùng chung
# Phép toán dịch bit : https://laptrinhcanban.com/python/nhap-mon-lap-trinh-python/so-trong-python/toan-tu-thao-tac-bit-trong-python/
r= ['--'.join((a.capitalize()+b.lower(),c.upper())) for a,b,c in [("hien","NAU","xinhdep"),("le","NGOC","hung")]]
print(r)
r= [[a,b,c] for a,b,c in [("hien","NAU","xinhdep"),("le","NGOC","hung")]]
print(r)
#Dùng vòng lập for:
r=[]
lt=[("hien","NAU","xinhdep"),("le","NGOC","hung")]
print(type(lt))
for a,b,c in lt: # Cách dùng rút gọn
	a=a.capitalize()
	b=b.lower()
	c=c.upper()
	print (["--".join((a+b,c))])
	r.append("--".join((a+b,c)))
print(r)
print({key:(value+1) for key, value in [("ns",93),("tuoi",30),("bienso",67)] if value% 2 != 0})
s={}
for key, value in [("ns",93),("tuoi",30),("bienso",67)]:
	if value % 2 != 0:
		#value += 1
		print (key,":",value)
		s.setdefault(key, value+1)
print(s)
s={}
for key, value in [("ns",93),("tuoi",30),("bienso",67)]:
	if value % 2 != 0:
		#value += 1
		print (key,":",value)
		s[key]=value+1
print(s)
lt= ["Hien","Nau","xinh","dep"]
print(list(enumerate(lt)))
for i,s in enumerate(lt,1):
	print("Chuoi thư",i,"la:",s)
print("Da het chuoi")
lst = [[1, 2, 3], [4, 5, 6]]
for i in range(len(lst)):
	for j in range(len(lst[i])):
		if j== 0:
			lst[i][j]= None
print(lst)
lst = [[1, 2, 3], [4, 5, 6]]
for i in range(len(lst)):
	lst[i][0]= None
print(lst)