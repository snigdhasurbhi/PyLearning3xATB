#Recursion is a programming technique where a function calls itself to solve a problem.
#Leet code= sum of digits of a number
#key concept
#base case
#recurssive case

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)# % remainder, // quioent, / divide
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(sum_of_digits(1235678))
print(factorial(5))

number=12345
r1=number%10
print(r1)
q2=number//10
print(q2)
r3=q2%10
print(r3)
q4=q2//10
print(q4)
r5=q4%10
print(r5)
q6=q4//10
print(q6)
n7=q6%10
print(n7)
n8=q6//10
print(n8)
n9=n8%10
print(n9)
n10=n8//10
print(n10)
n11=n10%10
print(n11)

