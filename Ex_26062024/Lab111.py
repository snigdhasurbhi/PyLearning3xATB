class Person:# class is the keyword, and person is the class name
    #Attributes
    name = "John"
    age = 30
    gender = "Male"
    phone_number = "1234567890"
    id = "123456"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    #Methods/Behaviour
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

    def talk(self): # no arg, no return
        print("I am talking")

    def walk(self):# no arg,with return
        print("I am walking")
        return "I am walking fast"

    def run(self,speed,time): #2 args with no  return
        print("I am running")

    def sleep(self, deep,early ): #args with return
        print("I am sleeping")
        return "I am in deep sleep"

#Create object of Person class
person1 = Person("John", 30) # objectreference_is person1 & object is Person()
print(person1) #Print the object
person1.greet()
person1.talk()
person1.walk()
person1.run(12, 34)
person1.sleep(2, True)
print(person1.name)
surya= Person("Surya", 25) # objectrefrence=object--->classname()
print(surya)
surya.greet()
ritika= Person("Ritika",25) # refernce is ritika and object is Person()
print(ritika)
ritika.greet()
