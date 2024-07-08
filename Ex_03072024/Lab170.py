with open("TestData.txt" , "r") as file:
    lines = file.readlines()

#print all lines
for line in lines:
    print(line, end=" ")