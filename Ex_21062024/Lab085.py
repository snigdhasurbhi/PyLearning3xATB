#tuple can also be called as immutable list
#tuple is can also be created by using function tuple(), but it can be empty
my_tuple=(10,20,30,40)
print(my_tuple)
t=tuple()
print(t)
print(type(t))
#we are converting/conversion list into tuple
t1=tuple(["ram","hanu","laxman","gopal","madan"])
print(t1)
print(type(t1))
#accessing tuple elements
print(t1[0])
print(t1[-1])
print(t1[1:3])
# my_tuple.copy()=t1
# print(my_tuple_copy)
#deleting tuple
# del t1
# print(t1) #TypeError: 'tuple' object is not callable

