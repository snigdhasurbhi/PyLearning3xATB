#web automation-selenium
#open the browser
# we will automate the process of opening the browser and navigating to a web page
class VWOLogin_page:
    email:None
    password=None

    def __init__(self,email,password):
        self.email= email
        self.password=password


    def login(self):
        print("Trying to login with " + self.email + " and " + self.password)
        #code to enter email and password
        if self.password == "password":
            print("Login successful")
        else:
            print("Not allowed to login")





amit=VWOLogin_page("amit12@gmail.com",  "password")
amit.login()
promod=VWOLogin_page("promode21@gmail.com","ssword")
promod.login( )






