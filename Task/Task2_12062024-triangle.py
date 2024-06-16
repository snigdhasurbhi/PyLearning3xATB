# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3
# Iso. = side 1 == side 2 != side 3
# Scalene = no sides are equal

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if side1 == side2 == side3:
    print("The triangle is equilateral.", "Eql")
if side1 == side2 != side3 or side1 == side3 != side2 or side2 == side3 != side1:
    print("The triangle is isosceles.", "Iso")
if side1 != side2 != side3:
        print("The triangle is scalene.", "Scal")
