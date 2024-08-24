#map, PICK one item and apply the functions to it and return the result
#filter, PICK one item and apply the functions to it and return the result if it satisfies the condition
#reduce, PICK one item and apply the functions to it and return the result if it satisfies the condition
#filter only work when it is true and flase condition
#map(function, iterable)
#map(function, iterable, iterable) #multiple iterables
#map(function, [])


# Example 1: Square each number in the list
numbers = [1, 2, 3, 4, 5]
def f(x):
    return x*x
new_numbers = map(f, numbers) #
squares_lambda=(list(map(lambda x: x*x, numbers)))
print(squares_lambda)
print(list(new_numbers))  # Output: [1, 4, 9, 16, 25]

#filters will keep only the items which satisfy the condition,if true then it will be there else not
# Example 2: Filter out even numbers from the list
def is_even(x):
    return x % 2 == 0
even_numbers = filter(is_even, numbers)#
print(list(even_numbers))  # Output: [2, 4]