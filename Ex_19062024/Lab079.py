#list collection of items in a particular order
my_list = [1, 2, 3]
my_list1= [1,"Snigdha", 20, 12.09]

#indexing
print("Enter the 0th index", my_list[0])
#changing an element
my_list[1]= 100
print("after changing the value", my_list)
#appending
my_list.append(4) # adding 4 in the end
print("after appending", my_list)
#extending
my_list.extend([4,5]) # extending 4,5 in the end
print("after extending", my_list)
#inserting
my_list.insert(1, 1000)
print("after inserting", my_list)

#removing
my_list.remove(3)
print("after removing", my_list)

#coping
list_copy = my_list.copy()
print("after coping", list_copy)

#deleting mylist
my_list.clear()
print("after clearing", my_list)
print("list_copy", list_copy)

#print 3rd index
#print("3rd index", my_list.index(3))

#sorting
list_copy.sort()
print("after sorting", list_copy)

#reversing
list_copy.reverse()
print("after reversing", list_copy)

print(list_copy[0])
print(list_copy[1])
print(list_copy[2])
print(list_copy[3])
print(list_copy[4])
print(list_copy[5])



