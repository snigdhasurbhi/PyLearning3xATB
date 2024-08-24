def decorator1():
    print("decorator1")
    def wrapper1(func):
        print("wrapper1")
        def inner1():
            print("inner1")
            func()
        return inner1
    return wrapper1

def decorator2():
    print("decorator2")
    def wrapper2(func):
        print("wrapper2")
        def inner2():
            print("inner2")
            func()
        return inner2
    return wrapper2
@decorator1()
@decorator2()
def display():
    print("display function ran")
display()
