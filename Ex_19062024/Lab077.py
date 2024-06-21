#even odd number
# def find_odd_even(num):
#     """Determines if a number is odd or even"""
#
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# print(find_odd_even(10)) # Output: even
check_evenodd =lambda num: "even" if num%2==0 else "odd"
print(check_evenodd(11))