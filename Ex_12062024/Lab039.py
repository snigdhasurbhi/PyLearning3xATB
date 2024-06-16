#Program for max number between two numbers
a=float(input("Enter number 1st\n"))
b=float(input("Enter number 2nd\n"))
#
result = max(a, b)
print(result)
def max_num(a, b):
    if a > b:
        return a
    else:
        return b


