class BankAccount:
    def __init__(self):
        self.balance= 0
        self.__private_var = 1000

    def public_fn(self):
        print(self.__private_evr)

    def deposite(self,amount):
        self.balance+= amount

    def _withdraw(self,amount): #protected
        self.balance-= amount

    def __show_bal(self): #private
        print(f"your balance is {self.balance}")

    def if_your_auth(self,flag):
        if flag:
            self.__show_bal
            print("u are allowed")

        else:
           print("you are not allowed")

    def if_you_auth_user(self,auth,amount):
        if auth:
            self.__withdraw(amount=amount)

        else:
            print("you wont be able to do withdraw")



jp_morgan= BankAccount()

print(jp_morgan.balance)
Secret_balance =input("enter the pin to see bal \n")
if Secret_balance =="1234":
    jp_morgan.if_your_auth(True)
else:
    jp_morgan.if_your_auth(False)

Secret_balance =input("enter the pin to desposite \n")
you_amount=int(input("enter the amount \n"))
if Secret_balance =="1234":
    jp_morgan.if_you_auth_user(True, you_amount)
    jp_morgan.if_your_auth(True)
else:
    jp_morgan.if_your_auth(False)

jp_morgan.deposite(307)
jp_morgan.if_you_auth_user(True,500)
jp_morgan.if_your_auth(True)

jp_morgan.show_bal()