
#Constructor
#self,init

class Demo_Person:
    name=None
    age=None
    id=None
    def __init__(self,name,age,id):# two types of constructor default constructor & parameterised constructor
        print("Constructor is executed")
        self.name=name
        self.age=age
        self.id=id
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.id}")

    def __init__(self): # default constructor without parameters
        pass

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id}"
    def m1(self):
        print("Method m1 is executed")


    def sleep(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
        print("who is sleeping -->" + self.name)

Person1=Demo_Person("John", 30, 1234)
Person1.sleep()
Person2=Demo_Person("Jane", 25, 5678)
Person2.sleep()
Person3=Demo_Person("Bob", 35, 9012)
Person3.sleep()