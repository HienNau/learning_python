a= id(5)
print(id(5))
print(a)
#https://www.youtube.com/watch?v=gw9zbl2Q7r4&list=PL33lvabfss1xczCv2BA0SaNJHu_VXsFtg&index=17
t=9
print(t+1)
print(t.__add__(1))
print(t.__sub__(1))
print(t.__mul__(2))
print(t.__radd__(1))
print(t.__rsub__(1))
print(t.__neg__())
#hashtable: tuple, string, number => immutable => pass py value
#unhashtable: list,set,dict => mutable =>pass by Reference
#Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”. In the event that you pass arguments like whole numbers, strings or tuples to a function, 
#the passing is like call-by-value because you can not change the value of the immutable objects being passed to the function. 
#Whereas passing mutable objects can be considered as call by reference because when their values are changed inside the function, then it will also be reflected outside the function.
#As a reference, int, float, bool, str, tuple, and complex are the most common types of immutable objects; list, set, and dict are the most common types of mutable objects.
#https://mathspp.com/blog/pydonts/pass-by-value-reference-and-assignment