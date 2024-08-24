class Parent:

    def __init__(self):
        print("i am snigdha")

class Son(Parent):
    def __init__(self):
        super().__init__()

S=Son() # when we create object the constructor will be called

