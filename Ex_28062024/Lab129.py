class Password:
    def __init__(self,password):
        self.__password= password
        self.public_var= 10

    def get_password(self,is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("invalid")

    def set_password(self,password): # modifing the data we need to use getter and setter in python
       if  len(password)>10:
           print("set to correct", self.password)
       else:
           print("not allowed")

pwd=Password("hacker1234")
pwd.get_password(True)
pwd.set_password("acb")# length should be 10
