#Loops means repeat a block of code multiple times
#There are two types of loops in python
#1. for loop
#2. while loop
# Print hello 10 times using for loop
for i in range(5): # 0 to 4
    print(i)
for i in range(1,5):  # 1 to 4
    print(i)
# range(start, stop, step) #start is inclusive, stop is exclusive
for i in range(1, 10, 2):  # 1 to 9 with step 2 only that is 1,3,5,7,9 not print 0,2,4,6,8
    print(i)
for i in range(10, 1, -2):  # 10 to 2 with step -2
    print(i)
    # Print 1 to 5 using while loop
i = 0
while i < 5:
    print(i)
    i += 1
    # Print hello 10 time using while loop
i = 1
while i <= 10:
    print("hello", i)
    i += 1
