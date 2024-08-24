# Encapsulation-warapping/hidding of the data, data binding, protecting the data
# Encapsulation - bind the data members,variables with the method, or class variable
# method are function within the class
# wrapping or binding the data meembers or class variable, or instance with the method
# hide the datamember(class variable, instance variable) by using only method

class Car:
    name=None
    password="123"
    def __init__(self):
        print("i am only called when object is created")
        print(f"hello my name is {self.name} and password is {self.password}")

    def change_password(self):
        self.password="17889"
        print(" password has been changed")
# this is the end of the class

XUV=Car() # when we had created object why constructor has not been called
XUV.password="67890"
XUV.name= "lam"
XUV.change_password()



