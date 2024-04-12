#Không thay đổi
a=[[1,2,3],[4,5,6],[7,8,9]]
b=a
b[0][0]="H"
print(a)
print(b)
#Vẫn không Thay đổi
a=[[1,2,3],[4,5,6],[7,8,9]]
b=list(a)
b[0][0]="H"
print(a)
print(b)
#Thay đổi rồi nè
a=[[1,2,3],[4,5,6],[7,8,9]]
b=list(a)
print(type(a))
print(type(b))
b[0]="H"
print(a)
print(b)
#Cũng thay đổi luôn nè
a=[[1,2,3],[4,5,6],[7,8,9]]
b=a.copy() # Giống b=list(a)
b[0]="H"
print(a)
print(b)
print(b.clear())
##https://www.youtube.com/watch?v=UzTE665WXb8&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=12
#https://www.youtube.com/watch?v=9IH3EynbcpU&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=13
t=["A","B","C"]
t.append("D")
print(t)
t.append(["D","E"])
print(t)
t=["A","B","C"]
t.extend(["D","E"]) #Thêm vào cùng cấp
print(t)
##
a=[[1,2,3],[4,5,6],[7,8,9]]
b=list(a)
b[0]="H"
a.clear()
c=a
print(a)
print(c)
#Hàm clear trả kết quả về None
a=[[1,2,3],[4,5,6],[7,8,9]]
b=list(a)
b[0]="H"
c=a.clear()
print(a)
print(c)
t=["A","B","C"]
t.insert(0,"K")
print(t)
print(t.insert(0,"K")) #=>Đáng lưu ý
t=["A","B","C"]
r=t.pop(2)
print(t)#Giống remove
print(r)
t=["A","B","C"] 
t.remove("A")
t=["A","B","C"]
t.reverse() #Giống print(k[::-1])
print(t)
t=["A","B","C"]
print(t[::-1])
t=["A","D","C"]
t.sort() #Hàm sort không hỗ trợ list có các kiểu dữ liệu khác nhau
print(t)