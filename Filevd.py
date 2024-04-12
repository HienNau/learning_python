file = open("Untitled-1.py", mode =("a+"))
data1 = file.readline()
file.seek(6)
data2=file.readline()
print(data1)
print(data2)
#Ví dụ tìm số lớn nhất
k1 = int(input("So thu nhat la:"))
k2 = int(input("So thu hai la:"))
k3 = int(input("So thu ba la:"))
if k1>k2 and k1>k3:
	print(k1,"la so lon nhat")
elif k2>k1 and k2>k3:
	print(k2,"la so lon nhat")
else: 
	print(k3,"la so lon nhat")
##############
file = open("Draft.txt",mode = ("r")) # Giống cú pháp: with open("Draft.txt","'r") as f:
arr = file.readlines() # Hoặc list(file)
print(arr)
new_content =""
for i in range(len(arr)):
	sub_arr=arr[i].split()
	for j in range(len(sub_arr)):
		if sub_arr[j]=="Kteam":
			sub_arr[j-1]= "How"
	new_content += " ".join(sub_arr)+"\n"
print(new_content)
with open("Kteam.txt","w+") as f:
	print(new_content,file=f) # Hoặc dùng câu lệnh f.write
