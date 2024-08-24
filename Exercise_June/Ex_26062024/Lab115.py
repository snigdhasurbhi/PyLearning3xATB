# calculator
class Calculator:
    def __init__(self, n1, n2):# when we have to assign the values, changes the value, run a special method while creating an object then we use construct
        self.n1 = n1
        self.n2 = n2
    def add(self):
        return self.n1 + self.n2
    def sub(self):
        return self.n1 - self.n2
    def mul(self):
        return self.n1 * self.n2
    def div(self):
        return self.n1 / self.n2

object_ref = Calculator(10, 99)# object_ref is object refernce &calculator() is object
print(object_ref.add())
print(object_ref.sub())
output=object_ref.mul()
print(output)
