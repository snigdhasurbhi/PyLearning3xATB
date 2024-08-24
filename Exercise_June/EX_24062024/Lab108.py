#without recussion
def sum_of_alldigits(n1):
    num=0
    while n1>0:
        num=num+n1%10
        n1=n1//10
    return num
print(sum_of_alldigits(123456789))

#without recursion
def factorial(n):
        fact=1
        for i in range(1,n+1):
            fact*=i
        return fact
print(factorial(9))