BaiTap = open ("BaiTap.csv",mode="r",encoding="UTF-8-sig")
BT = open("BT.csv", mode = "w+",encoding = "UTF-8-sig") # Không dùng mode a+ do con trỏ đưa về cuối file
BT.write(BaiTap.readline().strip()+ ",Điểm trung bình,Xếp loại\n") #write và read đưa con trỏ về cuối dòng
list_data = BaiTap.readlines()
print(list_data)
BaiTap.seek(0)
print(len(BaiTap.readline()))
for i in list_data:
	avg = round((float(i.strip().split(",")[2])+float(i.strip().split(",")[3]))/2,2)
	if avg >= 8:
		BT.write(BaiTap.readline().strip()+","+str(avg)+",Giỏi\n")
	elif avg >= 6.5:
		BT.write(BaiTap.readline().strip()+","+str(avg)+",Khá\n")
	else: 
		BT.write(BaiTap.readline().strip()+","+str(avg)+",Trung Bình\n")
BT.seek(0)
print(BT.readlines())
BT.seek(0)
print(list(BT))
BT.seek(0)
print(BT.read())
print(list(DictReader(BT.csv)))