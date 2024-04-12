i=[x for x in range(3)] # Trả kết quả là 1 list
print(i)
print(type(i))
i=(x for x in range(1,4))
print(i)
print(type(i)) #Kết quả trả về là generator, generator is a function that returns an object (iterator)
print(next(i))
print(next(i))
print(next(i))
l =[1,2,"Hien",[3,4]]
it =iter(l)
print(it)
print(type(it))
i=(x for x in range(3))
print(sum(i))
print(sum(i)) #Hàm sum phía trên đã đưa con trỏ về cuối dòng nên sd hàm next sẽ báo lỗi
i=(x for x in range(3))
print(sum(i,2))
i=(x for x in range(3))
print(max(i))
print(max([],default="HienNau"))
i=(x for x in range(3))
print(min(i))
it=[1,4,3,6,5]
print(sorted(it))
print(sorted(it,reverse=True))
string = "an,uong,cuoi"
print(sorted(string))
print(sorted(string.split(",")))
from datetime import *
to_day = datetime.now()
print(to_day)
print(to_day.second)