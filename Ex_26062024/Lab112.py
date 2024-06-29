class Dog: # class is keyword, name of the class is Dog
    #Attribute
    name = None # attribute, none means empty
    breed = None # attribute
    age = None # attribute
    color = None # attribute
    #Behaivour
    def bark(self): # method
        print("Woof!") # method body

    def talk(self): # method
        print("Barking") # method body

    def sleep(self): # method
        print("Zzzzzzz") # method body

    def eat(self): # method
        print("Nomnom") # method body

# Creating an object of the class
Tommy = Dog() # object name is Tommy and Dog is class name # object creation # object instantiation= Dog()
# THE MOMENT WE CREATED IT HAS OCCPIED NEW MEMORY
Tommy.name = "Buddy" # assigning value to the attribute
Tommy.breed = "Labrador" # assigning value to the attribute
Tommy.age = 3 # assigning value to the attribute
Tommy.color = "Brown" # assigning value to the attribute
# Accessing the attributes
print(Tommy.name) # Output: Buddy
print(Tommy.breed) # Output: Labrador
print(Tommy.age) # Output: 3
print(Tommy.color) # Output: Brown
# Calling the method
Tommy.bark() # Output: Woof!
Tommy.talk() # Output: Barking
Tommy.sleep() # Output: Zzzzzzz
Tommy.eat() # Output: Nomnom
tommy = Dog()
# Creating another object of the class
dog2 = Dog()
dog2.name = "CUTIE" # assigning value to the attribute
dog2.breed = "bULLDOG" # assigning value to the attribute
dog2.age = 5 # assigning value to the attribute
dog2.color = "WHITE" # assigning value to the attribute
# Accessing the attributes
print(dog2.name) # Output: Buddy
print(dog2.breed) # Output: Labrador
print(dog2.age) # Output: 3
print(dog2.color) # Output: Brown
# Calling the method
dog2.bark() # Output: Woof!
dog2.talk() # Output: Barking
dog2.sleep() # Output: Zzzzzzz
dog2.eat() # Output: Nomnom


