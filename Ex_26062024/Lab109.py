#class
#Object Demo
#Constructor
#self, _init_(),  __str__()
#take input and create a class
#class variable
#Method
#  # Public -variable- Dont mention anything
#Protected -
#Private-
#interitance
#Polymorphism
#Abstraction
#Encapsulation
#static Method, Variable
##
class Demo:
    def __init__(self):
        print("Constructor is executed")
    def m1(self):
        print("Method m1 is executed")
class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def  __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}"