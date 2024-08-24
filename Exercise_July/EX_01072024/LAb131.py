#Single
class Parent:
    gold="2kg"
    def Bhk2(self):
        print("2BHK")

class Child(Parent):
    def BHK3(self):
        print("3bhk")

object_ref= Child()
object_ref.BHK3()
object_ref.Bhk2()
print(object_ref.gold) # print parent class attribute

