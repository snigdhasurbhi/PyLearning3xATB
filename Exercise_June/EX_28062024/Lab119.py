class Person:
    # class variable , class attribute, static variable, instance variable
    # same for every instance of the class
    species = "Homo Sapiens" # class variable
    name = "John"
    age = None
    gender = "male"

    def walk(self):
        print("walking...")
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.species)
        print(Person.species)

Amit = Person()
Amit.name = "Amit"
Amit.walk()