#Function Scope
x = 10 # global variable
def my_function():
    x = 20 # local variable, they will be available only within the function not outside
    print("Inside the function, x is:", x)
    y = 30 # local variable
    print("Inside the function, y is:", y)
print(x) # it  has been called as x is acting as global function
#print(y) # it will throw an error because there is no intentation here, name 'y' is not defined
my_function()