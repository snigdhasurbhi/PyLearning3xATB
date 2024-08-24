# tuple of vowels-collection of item while tuple is immutable in nature
vowels = ('a', 'e', 'i', 'o', 'u')
my_list=[2,4,67,89,4,78]# list are mutable in nature
print(id(my_list))


my_list.extend(vowels)
print(id(my_list))
my_list[0]=28
print(my_list)

#tuple is same as list but in round bracket and we can change the value
my_tuple=(2,4,67,89,4)
print(id(my_tuple))
#my_tuple[0]=28 # if do this will get an error that tuple object cant be changed, TypeError: 'tuple' object does not support item assignment
print(my_tuple)
print(my_tuple[0]) # we can access the element of tuple using index number

# my_tuple.sort() #AttributeError: 'tuple' object has no attribute 'sort'
# print(my_tuple)

my_tuple+=vowels
print(my_tuple)
#my_tuple.append(100) # attribute error
my_tuple=my_tuple+vowels
print(my_tuple)

# my_tuple.reverse() #AttributeError: 'tuple' object has no attribute 'reverse'
# print(my_tuple)

my_tuple.remove(4)
print(my_tuple)

my_tuple.pop(2)
print(my_tuple)

my_tuple.insert(0, 100)
print(my_tuple)

my_tuple_copy=my_tuple
print(my_tuple_copy)

my_tuple.clear()
print(my_tuple)



