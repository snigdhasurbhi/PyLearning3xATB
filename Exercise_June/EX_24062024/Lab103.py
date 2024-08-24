# filter in the python, kind of like a for loop but it filters out the values that we don't want
# its a buit in function filter()
#allows you to filter elements  in tuple,List,set
#filter always works with function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]
def is_even(input_list):
    return input_list % 2 == 0
new_even_numbers = filter(is_even, numbers)
print(list(new_even_numbers))  # Output: [2, 4, 6, 8, 10]

def greater_than_five(input_list):
    return input_list > 5
new_greater_than_five = filter(greater_than_five, numbers)
print(list(new_greater_than_five))  # Output: [6, 7, 8, 9, 10]


