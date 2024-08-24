
def outer_function(name):
    var1=30
    def inner_function():# inner function can access the global variable as well as outter function var
        print(f"Hello, {name}")
        print(var1)
    return inner_function()
outer_function("John")