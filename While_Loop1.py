k=3
while k > 0:
	print("k=", k)
	k= k-1
st= "Hien Nau"
index= 0
lenstr = len(st)
while index < lenstr - 1:
	print(index,"Ki tu hien tai la:",st[index])
	index += 1
if index == lenstr - 1:
	print (index,"Day la ki tu cuoi cung:", st[index])
ls =[]
k=1
while True:
	if k % 2 == 0:
		ls.append(k)
		if len(ls) == 5:
			break
	k +=1
print(ls)
print(k)
ls =[]
k=1
while len(ls)<=5:
	if k % 2 == 0:
		ls.append(k)
		if len(ls) == 5: # vòng lặp b nàm trong vòng lặp a thì b chứa break sẽ dừng b, còn a thì không
			break
	k +=1
print(ls)
k=1
ls=[]
while len(ls) <5:
	k+=1
	if k % 2 != 0:
		continue
	ls.append(k)
print(ls)
print("So k cuoi cung la:",k)
k= 0
while k<10:
	k+=1
	if k % 2 == 0:
		continue
	else: 
		print(k,"is an odd number")
print(k)
k= 0
while k<10:
	k+=1
	if k % 2 == 0:
		continue
	print(k,"is an odd number") # Giống ở trên (rút gọn else)
print(k)
k = 0
while k<=3:
	print("GT cua k hien tai la:",k)
	k+=1
	if k ==2:
		break #Gặp break thì else không được thực hiện
else:
	print("k da lon hon 3")

arr= [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
print(sorted(arr)) #Chỗ này ôn lại

arr= [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
i= 0
j= 0
while i < len(arr) -1:
	if arr[i] == 11:
		i+=1
		continue
	j=i+1
	while j < len(arr) :
		if arr[j] == 11:
			j+=1
			continue
		elif arr[i] > arr[j]:
			arr[i],arr[j] = arr[j],arr[i]
		j+=1
	i+=1
print(arr)