s={(1,2),"HienNau"}
print(s) # set không chứa kiểu dữ liệu unhashable
#print (s[0]) => báo lỗi, không hỗ trợ truy cập theo index
s={1,1,1,1,1}
print(s)
# Không thể tạo 1 empty set
s={}
print(s)  # Trả về kiểu dữ liệu là dict {}
s={i for i in range(3)}
print(s)
s= set()
print(s) # Tạo 1 empty set set()
s= set([1,1,2,2]) #Khác với tạo set bằng dấu {}
print(s)
print("ham set {0} - {1}".format(s,111))
print("Ket qua la: ",3 in s)
a={1,2,3}
b={1,2,6}
print(a-b)
print(a&b)
print(a|b)
print(a^b)
a.clear()
t=a.clear()
print(a)
print(t)
print(a.clear()) #Giống với list
s={1,2,3}
t=s.pop() #Không có thứ tự vị trí của phần tử trong set
print(s)
print(t)
s= set()
#t=s.pop()
# print(t) => Báo lỗi
s={1,2,3}
s.remove(1)
print(s)
s={1,2,3}
s.discard(2)
print(s)
s={"a","b","c"}
s.discard("d") #Giống remove nhưng không báo lỗi khi phân tử không tồn tại trong set
print(s)
s={"a","b","c"}
t=s.copy()
print(t)
s={"a","b","c"}
print(s.add("d")) # => Đáng lưu ý
s={1,2,3}
s.add(0)
print(s)
s1={1,2,3}
s2=s1.copy()
s2.clear()
print(s2)
print(s1)
s1={1,2,3}
print(len(s1))
print(len(s1))
s={1,2,4,1,2,3}
print(s) #Tự động bỏ các phần tử trùng và tự động sort