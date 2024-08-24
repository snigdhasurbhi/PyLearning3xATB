#indentationError
#  print("dad")#indentationError

# result =5+"5" # TypeError: unsupported operand type(s)for +: 'int' and 'str'

# int("snigdha") # ValueError: invalid literal for int() with base 10: 'snigdha'

# print(undefin_variable) # NameError: name 'undefin_variable' is not defined


# my_list =[1,2,3]
# print(my_list[3])  #IndexError: list index out of range

# my_dict = {"a":1 , "b":2}
# print(my_dict["c"])  #KeyError: 'c'

# result = 10/0     # Zero Division Error

#import non_existent_module    #ModuleNotFoundError: No module named 'non_existent_module'


# import math
# math.exp(1000)    #Overflow Error: math range error


try:
    import math
    math.exp(1000)
except Exception as e:
    print(e)
