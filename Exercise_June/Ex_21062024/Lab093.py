set2={"testing acemdmy", "testing requirements", "testing done"}
print(set2)
for i in set2:
    print(i)
set1=set([4,5,67,7,8,9,
          5,8,9,0,2,1,4,3])
print(set1)
set3=set1.copy()
print(len(set1))
print(set3)
set1.remove(4)
print(set1)
set1.add(11)
print(set1)
set1.pop()# remove the first item
print(set1)
set1.clear()
print(set1)
print(len(set3))

