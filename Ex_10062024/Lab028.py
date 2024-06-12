#OPErators
#Assignment Operator
# =- assign the value from right to left
name = "Rahul"
a = 10

#Compare operator
# == - equal to (bool)
V1=(1==True)
print(V1)
V2=(0==True)
print(V2)
V3=(0==False)
print(V3)
# != - not equal to
# < - less than
# > - greater than
# <= - less than equal to
# >= - greater than equal to

#Logical operator
# and
# or
# not

#Bitwise operator
# & - AND
# | - OR
# ^ - XOR
# ~ - NOT
# << - Left shift
# >> - Right shift

#Identity operator
# is
# is not

#Membership operator
# in
# not in

#Ternary operator
# condition_if_true if condition else condition_if_false

# unary operator
age=55
age1= +57 # pycharm will remove the + sign as its self explanatory
age2= -57 # pycharm will not remove the - sign
print(age)
print(age1)
print(age2)
print(type(age2))
num= 24
r=(age2+num) #addition -57
print(r)
r1=age2-num
print(r1)

# not operator is used to reverse the boolean value

is_married= False
print(not is_married)

#is operator is used to check if the two variables are pointing to the same object
#is operator is used mostly in the case of List and Dictionary
x=10
y=10
z=False
a=5
b=6
print(x is y)
print(x is z)
print(a is b)
My_list=[1,2,3,4,5]
My_list1=[1,2,3,4,5]
print(My_list is My_list1) #false because they are pointing to different objects
My_list2=My_list1
print(My_list2 is My_list1) #true because they are pointing to the same object

