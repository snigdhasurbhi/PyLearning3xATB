#ternary operator is a if else condition in one line
x=10
y=20
print(x if x>y else y)# condition true then x else y

a=int(input("enter a number:"))
b=int(input("enter b number:"))
print("b is winner" if b>a else "a is winner")

if b>a:
    print("b is winner")
else:
    print("a is winner")