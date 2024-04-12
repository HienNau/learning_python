a= 4
if a - 1 <0:
	print("a < 1")
elif a- 2 <0:
	print("a<2")
elif a- 3 <0:
	print("a<3")
else:
	print("a>=3")
a= 0
if a - 1 <0: print("a < 1") ; print("a nhỏ hơn 1")
#a=int(input("Nhap so:")) # Làm bài tổng kết mà chưa biết làm
#print(a)

lst = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]

idx = 0
maidx = len(lst) - 1

majdx = len(lst)

while idx < maidx:
    if lst[idx] == 11:
        idx += 1
        continue
    jdx = idx + 1
    while jdx < majdx:
        if lst[jdx] == 11:
            jdx += 1
            continue
        if lst[idx] > lst[jdx]:
            lst[idx], lst[jdx] = lst[jdx], lst[idx]
        jdx += 1
    idx += 1
print(lst)
