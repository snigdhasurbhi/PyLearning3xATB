#Python
my_dict = {
    'name': 'Nicolas',
    'age': 90,
    'last_name': 'Gonzalez'
}
#to find the key
for k,v in my_dict.items():
    if v == 90:
     print("value with key 'age' is 90")
     break
     #to find the value
for k,v in my_dict.items():
    if k == 'age':
     print("key with value 90 is 'age'")

op=90 in my_dict.values()
print(op)

