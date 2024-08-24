#

class Vmwologin:
   def login(self,Email,Password):
       if self.Password == "Password":
        print("Login succesful" )
       else:
           print("You are not allowed")



Email=input("enter your email address \n")
Password=input("enter your password \n")
amit=Vmwologin()
amit.login(Email,Password) # without creating constructor why we are not able to call input data
Email=input("enter your email address \n")
Password=input("enter your password \n")
promod=Vmwologin()
promod.login(Email,Password)