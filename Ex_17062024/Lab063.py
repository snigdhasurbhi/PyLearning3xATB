#agrs
def print_arguments(args):
 print("hello")

print_arguments(5)

def print_arguments1(*args):# number of arguments, similar to list
 for i in args:
     print(i,end= '\n')
print_arguments1("amit", "durga", "ram")


#args-list
a=["om","namesh", "shiva"]
for i in a: # we have taken list, for iterate the list
    print(a)
    print(i)
for i in range(1,5): # we have taken range for the number from 1-4
    print(i)