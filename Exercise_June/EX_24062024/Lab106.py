#Recurrsion it is a function which calls itself in order to solve a problem
#key Concept,
#1.base case
#2.Recursive case
#Factorial of a number
def factorial(n):
    if n == 0:#base case
        return 1
    #recursion case
    else:
        return n * factorial(n-1)
print(factorial(5))#120
num=(int(input("Enter the number")))
print(factorial(num))
