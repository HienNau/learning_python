print("Nguyen","Thi","Thu","Hien")
i= float(8.9)
print(i)
print(int(float("6.9")))
print("Hien"+"99") #Noi string bằng + sẽ trả kết quả không có khoảng cách
print("Hien"+"\n"+str(99))
print("Hien","99",end="\t")
print("Hien","99",sep=" -- ")
#from time import sleep
#print("end")
#from time import sleep
#print("start",end="")
#sleep(3)
#print("end")

from time import sleep
print("Batdau",end="")
sleep(3)
print("Ketthuc")
from time import sleep
print("start",end="",flush=True)
sleep(3)
print("end")
a= "HienNau"
b="NguyenThiThuHien"
for c in a + b:
	print(c,end="",flush=True)
	sleep(0.5)
with open("HienNau.py","w+") as f:
	print("Hien",file=f)