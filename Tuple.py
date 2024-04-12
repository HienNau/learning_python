T= tuple([1,2,3])
print(T)
print(type(T))
t=(n for n in range(10))
T=tuple(t)
print(T)
r= (1,2,3)
r+=(4,5,6)
print(r)
r= (1,2,3)
r*=3
print(r)
r= (1,2,3)
print(4 in r)
r= (1,2,3)
print(r[1])
r= (1,2,3)
print(r.index(1))
r= (1,2,3)
print(len(r))
r= (1,2,3)
print(r[-1])
#tuple và chuỗi là 1 dạng hash object giống nhau về các toán tử
#tuple không thay đổi nội dung được giống như list
#tuple cũng có ma trận giống như list
r= ([1,2,3]) #Bên trong tuple là 1 unhash object (1 list) thì có thể thay đổi nd tuple được
r= (1,2,3,1)
print(r.count(1))
r+=(4,) #Viết (4) thì python hiểu là kiểu int
print(r) #Kiểu tuple không có hàm append nên phải dùng phương thức +=
#https://www.youtube.com/watch?v=dDFFCbRGm3o&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=14 => Vì tuple là hash object nên không dùng lam dictionary
