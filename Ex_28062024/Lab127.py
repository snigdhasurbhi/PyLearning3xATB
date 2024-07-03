class VWLogin:
     def __init__(self,email,password, name):
         self.__email=email # double underscore is private
         self.__password=password #single underscore is protected
         self.name= name

     def login_Confirm(self):
            if self.__email == "abc@gmail.com" and self.__password == 123 :
                print("your login is succesful")
            else:
                print("you are not allowed")

#this is the end of class

page=VWLogin("abc@gmail.com",123, "ram")
print(page.name)
page.login_Confirm()