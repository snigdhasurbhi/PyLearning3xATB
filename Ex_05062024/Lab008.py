# Dynamically types means that the type of a variable is determined at runtime,
# Dynamically typed languages are those that do not have to specify the type of a variable at compile time.
# Dynamic type = Type of Data that Python supports
age = 65
# Variable age is of type int
# variableName =variableValue
# identifier = literal

# Data type
# int = integers= +ve and -ve numbers, whole number
# float = decimal numbers, 3.14, 18.00, 0.0009988,  -0.0009988, -1.65
pi = 3.14
# str = string- anything in between "" or '', a banch of characters = "Hello World",  'Hello World',  '123',  '3.14',   'True', "A"
name = "John"
# bool = boolean = True, False, (true, false) is not case sensitive/ not a boolean,  (True, False) is a boolean
ismarried = True
# None = null, empty value, nothing
# None is a data type in python
# list = [] - empty list
# tuple = () - empty tuple
# How do we check the type of a variable?
print(type(age))
print(type(name))
print(type(pi))
print(type(ismarried))

# python- ComplexNumbers -i iota- imaginary number
Complex_number = 3+5j
#Complex_number = 3+5j = a+bi
# a = real part
# b = imaginary part
# a+b = real part
# a-b = imaginary part
print(Complex_number.real)
print(Complex_number.imag)
