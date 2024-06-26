#tuple each value is assigned, unpacking of the tuple assigning to different variable
#unpacking of tuple
x=35
a,b,c,d=(23,67,90,57)
print(a,b,b,d)
print(id(a))
print(b)
print(c)

cities = ("London", "Paris", "New York", "Amsterdam")
print(cities)
print(type(cities))
print(cities[0])
print(cities[-1])
print(cities[1:3])
print("Dubai" in cities)
for city in cities:
    print(city)