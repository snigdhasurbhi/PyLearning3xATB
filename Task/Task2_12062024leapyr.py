#Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Output the result using a suitable message.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a leap year.")

# year = int(input("Enter a year: "))
# def is_leap(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 return True
#             else:
#                 return False
#         else:
#              return True
#     else:
#         return False
#
#
# print(is_leap(year))