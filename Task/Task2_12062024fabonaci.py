#4. Fibonaci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13
n= int(input("Enter a number: "))
a=0
b=1
print(a)
print(b)
for i in range(1,n):
    c=a+b
    a=b
    b=c
    print(c, end=" ")

