# Question 1 Explain the difference between the = operator and the == operator in Python.
a = 12 # Assignment operator The operator is used to assign a value to a variable. It stores the value on the right-hand side in the variable on the left-hand side.
b = 12 #Assigns the value 12 to the variable b.
c="john" #Assigns the String value "john" to the variable c.
print(a)
print(a==b)
print(a==c)
#The == operator compares two values and returns True if they are equal, and False otherwise.
#The = operator assigns a value to a variable.



# Question 2 Explain the difference between the += operator and the + operator in Python.
x=20
y=30
x+=y #x=x+y i.e x=20+30=50 +=  operator is used to add two numbers or concatenate two strings
print(x+y) #50+30=80 + operator is used to add two numbers or concatenate two strings
print(x) #x=50
#The main difference is that the +operator creates a new list object, while the
#+= operator modifies the existing list in-place.
a = [1, 2, 3]
b = [4, 5, 6]
a += b # += operator is used for in-place addition or concatenation. When used with lists, it modifies the original list by appending the elements from the right-hand side operand to the end of the left-hand side operand.
print(a)  # Output: [1, 2, 3, 4, 5, 6]

c = [7, 8, 9]
d = [10, 11, 12]
e = c + d # The original lists c and d remain unchanged.
print(e)  # Output: [7,8,9,10,11,12]
print(c)
print(d)



#What does the ** operator do in Python, and how is it used?
result = 2 ** 3  # 2 raised to the power of 3
print(result)    # Output: 8
#In Python, the ** operator is known as the exponentiation operator or the power operator. It is used to raise a number to a given power.
# Exponentiation: When used with two numeric operands, the ** operator raise the first operand to the power of the second operand
#Power of a negative number: The **operator can also be used with negative numbers as the exponent.
result1 =2**-3
print(result1) # 1/8=0.125  2 raised to the power of -3
result2 =-2**3
print(result2) # -2*-2*-2=-8,  -2 raised to the power of 3 = -8




#What does the ^ operator do in Python, and in what context is it commonly used?
# *** In Python, the ^ operator is the bitwise XOR (exclusive OR) operator. It performs the XOR operation on the binary representations of the operands, bit by bit. [1]
# The XOR operation follows these rules: [2] If both bits are 0, the result is 0.
# If both bits are 1, the result is 0.
# If one bit is 0 and the other is 1, the result is 1.
# The ^ operator is commonly used in the following contexts:
# Bitwise Operations: The ^ operator is used for bitwise manipulation of integers. It can be useful when working with low-level operations, such as encryption, compression, or network protocols.
e = 8    # Binary 8 bit: 1000
f = 9    # Binary: 1001
g = e ^ f  # Bitwise XOR: 0001 (Result: 1)
print(g)  # Output: 1
# *** Swapping Values: The ^ operator can be used to swap the values of two variables without using a temporary variable. This is a common trick in programming interviews and coding challenges
h = 5
i = 7
h = h ^ i  # a = 5 ^ 7 = 2
i = h ^ i  # b = 2 ^ 7 = 5
h = h ^ i  # a = 2 ^ 5 = 7
print(h, i)  # Output: 7 5