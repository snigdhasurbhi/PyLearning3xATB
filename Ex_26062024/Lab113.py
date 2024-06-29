#constructor uses for intialise the value
#contructor of the instance variable
#Constructor
class Person:
    name=None #instance variable
    age=None
    id=None


    def __init__(self, name, age):# init is function which is used for constructor, self is used for point to current object, name and age is parameter,
        self.name=name #self.name=name is used for assign the value to instance variable,
        self.age=age # self.age=age is used for assign the value to instance variable.
        print("Constructor is called")
        print(f"Name: {self.name}, Age: {self.age}") # self is same as this in java
        print(id(self))
        print("--------------")
        # self.id=id(self)
    #Methods/Behaviour
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
        print(id(self))
        print("--------------")
        # self.id=id(self)

p1=Person("John", 30)
p2=Person("Jane", 25)
p1.greet()
p2.greet()
print(id(p1))
print((p2.greet()))