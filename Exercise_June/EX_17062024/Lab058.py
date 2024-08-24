#function
#block of code
#define, call
#builtin.py function-which is created by the python contributor

#user define
#they can return something
#they can't return something
# they have parameters
# they dont have parameters
#define
def say_hello():
         print("hello")

       #call
say_hello()

def say_hello_args(name):#no return type with arguments
    print(name)
say_hello_args("Snigdha")
say_hello_args("Surbhi")

def say_hello_args_default(name="Snigdha"): #no return type with default arguments
    print("hello", name)

say_hello_args_default()# we are not passing any argument,so it will take default value
say_hello_args_default("Deep") #we are passing value
say_hello_args_default(name="harsha") #we are passing value

#
def sum_num_arg_ret(a,b):#with arg and return type
 return a+b
# result=sum_num_arg_ret(a=40,b=30) # here we should know the defination of the function then only we will able to inital the value,i.e a,b
result=sum_num_arg_ret(20,30)
print(result)


