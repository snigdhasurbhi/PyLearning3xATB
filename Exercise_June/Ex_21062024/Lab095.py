# DEcorators in python means essentially function that takes another function as an argument and extends its functionality
# In other words, a decorator is a function that takes another function and returns a new function that enhances the original function
#DEcorators return a new function with the added functionality, without modifying the original function
def decorator_function(original_function):
    def wrapper_function():
        print("starting..........................")
        print("***************************************")
        print(f"Wrapper executed before {original_function.__name__}")
        original_function()#this will execute the display function
        print("***************************************")
        print("ending..........................")
        #return original_function()
    return wrapper_function
# Example 1
@decorator_function #this is the same as saying display=decorator_function(display)
def display():
    print("Display function ran")
#display=decorator_function(display)
display()
