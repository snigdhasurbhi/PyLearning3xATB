#Logical operators- boolean
#and
#or
#not

a=30
b=20
print(a>b)
print(a<b)
print(a>b and b>a)
print(a>b or b>a)
print(not a>b)
print(a>b and b>a)
print(not a) #false because 0 is false, rest all are true

x=50
y=50
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y) #greater than or equal to 50> 50 or 50 =50
print(x<=y) #less than or equal to

#or gate
print(x>y or x==y)
f=False
t=True
print(f or t) #true because f is false following the truth table of and
print(f and t) #false because f is false following the truth table of and
print(f and f) #false because f is false