#Multiple conditional
#problem find the max between 3 numbers
#num1,num2,num3
#num1 >num2 and num1>3 =num1
#num2>num1 and num2>num3 = num2
# num3
num1 = float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print("The largest number is num1")
elif num2 >= num1 and num2 >= num3:
    print("the largrest number is num2")
else:
    largest = num3
    print("The largest number is", largest)