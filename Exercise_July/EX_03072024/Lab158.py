# Custom exception
class MyCustomException(Exception):# for making own exception we need to inherate exception in class
    def __init__(self,message):
        self.message=message +"low"
        super().__init__(message)# super is calling the parent constructor
balance =100
withdraw= int(input("Enter the number"))
if  withdraw >balance:
    raise Exception("balance is low")
else:
    print("remaining balance", (balance-withdraw) )

