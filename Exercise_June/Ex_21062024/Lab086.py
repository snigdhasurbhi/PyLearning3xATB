#
hero1=("Batman","SPiderman","antman","waspman","ironman")
hero2=("Hulk", "Thor", "Hawkeye", "Vision", "Black Widow")
tuple=(hero1+hero2)
print(tuple)
print(tuple[1][5])#indexing for 1st value's in the 5th number
print(len(tuple))#length
print(tuple.count("SPiderman"))#on which count spider man is in
print(tuple[2])# in the second index
print(tuple[0:3])# in the 0 to 3 index
print(tuple[-1])# in the last index
print(tuple[1:4])#in the 1to4 index
print("SPiderman" in tuple)#in the operator is Spider present in the tuple or not
print("Falcon" in tuple)#in the operator
for i in tuple:
    print(i)
    if i=="Vision":
        break
        print("Hello")

