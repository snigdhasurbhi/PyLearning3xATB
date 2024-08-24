#
List=[2,45,7,8,34,67]
# print(List*2)# it will print the list twice
# print(List+List)# it will print the list twice

temp_list=[] #creating the new list for storing the double value
for item in List:
    # temp=item*2
    # temp_list.append(temp)
    temp_list.append(item*2)# it will print the list twice
    print(temp_list)#  it will print the list twice,it is forming triangle because of indentation
print(temp_list)