#Right triangle number pattern
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
a = 1
for i in range(1, 7):
    for j in range(1, i+1):
        print(a, end=" ")
        a += 1
    print()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
num=(int(input(f"enter the number for which u need to print right triangle")))
print(num)
b = "*"
for i in range(0, num):
    for j in range(1, i+1):
        print(b, end=" ")
        b += "*"
    print()

val=(int(input("Enter the value till which you wanted to print triangle" " " )))
for i in range(0,val+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
row = ""
for i in range(0, len(letters)):
    row = row + letters[i]
    print(row)