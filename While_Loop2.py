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
    if k % 2 == 0:
        k+=1
        continue
    else: print(k,"is an odd number")
    k+=1
print(k)
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (list(enumerate(l1))) #Giống dict.items (phải đưa về dạng list)
  
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))