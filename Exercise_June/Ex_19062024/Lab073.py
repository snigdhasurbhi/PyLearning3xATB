#list collextion of item
num=[1,2,45,67]
def do_something(num_name): # we have passed whole list
    num_name.append(69) #appending it
    num_name[0]=200,4,6 #we are passing 200 in the 0th place of num
    return num_name # while

num.append(19)
l=do_something(num) # we are passing whole list as argument
print(l)