#Access modi
class car:
    name= None


    def __init__(self):
        self.public_var= "public"
        self._protected_var="12334"
        self.__private_var= "werrt"
    def __private_method(self):
        print("Private method called")

    def _protected_method(self):
        print("Protected method called")
        if self.__private_var=="wehfhxuyrt":
            print(f"hi {self.public_var} i am {self._protect_var}")
        print("Private var accessed from protected method")

    def __private_method(self):
        pass


# this is the end of the class
Aulto=car() # aulto obj.ref, car() is object
Aulto.publi_var= "hahaha"
Aulto._protect_var="3gwtwr"
Aulto.__private_var="wehfhxuyrt"
Aulto._protected_method()
print(Aulto.public_var)





