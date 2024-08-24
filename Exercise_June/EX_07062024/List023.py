#List-Shopping list
#List-Items in the list
#List-Add item to list
#List-Remove item from list
#List-Print list
#List-Print item at index
#List-Print length of list
#List-Print list in reverse
#view
#exit

shopping_list = ["milk,bread,butter,poha"]
print(shopping_list)
shopping_list = ["milk","bread","butter","poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[1])
my_list = ["milk","98900","soap","poha"]
print(my_list)
print(type(my_list))
my_list.append("curd") #add item to list in last
print(my_list)
my_list.remove("soap")
print(my_list)
my_list.insert(2, "jam") #add item at specific index
print(my_list)
my_list.pop() #remove last item
print(my_list)
my_list.reverse()
print(my_list)
my_list.extend(["chips,Salt"])
print(my_list)
my_list.extend(["candy","straw"])#add multiple items in the end
print(my_list)
my_list.sort()