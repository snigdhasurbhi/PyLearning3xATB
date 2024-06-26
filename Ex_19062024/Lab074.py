ortant question
#Lambda Expression= to do the task in a single line of code
# 1. what is the output of the following code?
# numbers = [1.0, 2.0, 3.0, 4.0]
#
# def double_salary(salary):
#     return salary * 2
# #new_salaries = list(map(double_salary, numbers))
# new_salaries=double_salary(100)
# print(new_salaries)
f_double_salary=  lambda salary: salary * 2
print(f_double_salary(100))