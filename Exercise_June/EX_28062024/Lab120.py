class car:
    name = None
    speed = None
    color = None
    make = None
    model = None

    def __init__(self,name,make,speed,color,model):
        self.name = name
        self.speed = speed
        self.color = color
        self.make = make
        self.model = model

    def  drive(self):
        print(f"The {self.color} car is driving at {self.speed} km/h.")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
    def start_engine(self):
        print("Vroom! The engine has started.")
        print(f"Vroom! The engine has started. car color is {self.color} at the speed of {self.speed} km/hr model number is {self.model} ")
        print("Vroom! The engine has stopped.")
#this is the end of the class

lamborghini = car("Lamborghini", "Lamborghini", 300, "yellow", "Aventador")
lamborghini. drive()
lamborghini.start_engine()
print("===============================================")
ferrari = car("Ferrari", "Ferrari", 200, "red", "Enzo")
ferrari. drive()
ferrari.start_engine()
print("===============================================")
porsche = car("Porsche", "Porsche", 150, "black", "911")
porsche. drive()
porsche.start_engine()
print("===============================================")
audi = car("Audi", "Audi", 100, "white", "A4")
audi. drive()
audi.start_engine()
print("===============================================")
bmw = car("BMW", "BMW", 50, "blue", "5 Series")
bmw. drive()
bmw.start_engine()
print("===============================================")
