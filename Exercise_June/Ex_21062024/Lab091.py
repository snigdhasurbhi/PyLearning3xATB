t=("testing acedmy for testers", "python for data science", "python for machine learning")
print(t)
print(type(t))
print(t[0])
print(set(t))# converted tuple into set
print(list(t))# converted tuple into list
print(tuple(t))# converted tuple into tuple
set1={7,9,0,8}
set2={1,2,7,6,4,5,8}
my_set=set1.union(set2)
My_set_intersection=set1.intersection(set2)
print(my_set)
print(My_set_intersection)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))