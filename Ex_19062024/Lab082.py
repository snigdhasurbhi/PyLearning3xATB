# doubling item using  map function and lambda

def double_item(item):
    return item * 2
def add2_item(item):
    return item + 2
def divide_item(item):
    return item / 2

def power_item(item):
    return item ** 2

# def subs_item(item): instead of using this function we can use lambda function
#     return item - 2

substract=lambda item:item-2

# def mod_item(item): # instead of creating funct we used lambda
#     return item % 2
#
# mod=lambda item: item%2 # instead of creating lambda function here we will use inside the map


#map function,map() without using for loop we can excute
#take each item from list and pass it to the function
#return the same number of the element(list)
#Return a map object which is an iterator of results after applying the given function to each item of a given iterable
list1=[1,2,3,4,5]
# double_list=map(double_item,list1)
# print(list(double_list))
double_list=list(map(double_item, list1))
print(double_list)

add2_list=list(map(add2_item, list1)) # we use list() to convert map object to list else provide map object
print(add2_list)

divide_list=list(map(divide_item, list1))
print(divide_list)

power_item=list(map(power_item, list1))
print(power_item)

substract=list(map(substract, list1))
print(substract)

mod_list=list(map(lambda item: item%2,list1))# here using lambda
print(mod_list)

print(list(map(lambda number: number*3,[3,4,5,6,7] )))# in one line we can use lambda function
