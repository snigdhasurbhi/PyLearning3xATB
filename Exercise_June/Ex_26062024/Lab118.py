class Solution:
   def __init__(self):
      self.name = input("Enter your name: ")
      self.age = int(input("Enter your age: "))
      self.id = int(input("Enter your id: "))
      self.salary = float(input("Enter your salary: "))
      self.address = input("Enter your address: ")
      self.contact = input("Enter your contact: ")
      self.email = input("Enter your email: ")
      self.qualification = input("Enter your qualification: ")
      self.experience = input("Enter your experience: ")
      self.basic_salary = float(input("Enter your basic salary: "))

   def display(self):
      print(f"Name: {self.name}")
      print(f' hello my  name is {self.name},i am {self.age}year old,my id is  {self.id},earn {self.salary}, live in {self.address}, below is my contact address {self.email} & number {self.contact}, my qualification is {self.qualification},i have {self.experience} yesars of expereince, with {self.salary} ')
      print(f"Age: {self.age}")
      print(f"Id: {self.id}")
      print(f"Salary: {self.salary}")
      print(f"Address: {self.address}")
      print(f"Contact: {self.contact}")
      print(f"Email: {self.email}")
      print(f"Qualification: {self.qualification}")
      print(f"Experience: {self.experience}")
      print(f"Basic Salary: {self.basic_salary}")
Stdd=Solution()
Stdd.display()