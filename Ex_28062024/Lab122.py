#without using constructor

class VWOLogin_page:
    email:None # class variable, attribute
    password=None


    def login(self):
        print("Trying to login with " + self.email + " and " + self.password)
        #code to enter email and password
        if self.password == "password":
            print("Login successful")
        else:
            print("Not allowed to login")


amit=VWOLogin_page()
amit.email= "amit12@gmail.com"
amit.password= "password"
amit.login()
promod=VWOLogin_page()
promod.email= "promode21@gmail.com"
promod.password= "ssword"
promod.login( )

