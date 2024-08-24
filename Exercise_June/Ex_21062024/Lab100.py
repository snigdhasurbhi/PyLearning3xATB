promode_details ={
    'name': 'promode',
    'id': 1,
    90: 5.6,
    'address':'kathmandu',
    "is_active": True
 }
print(promode_details)  # {'name': 'promode', 'id': 1, 90: 56, 78: None, 'address': 'kathmandu', 'is_active': True}}
print(promode_details.get('name')) #promode, we have to mention the name of the key
print(promode_details.get('id')) #1
print(promode_details["address"]) #'kathmandu'
print(promode_details[90]) #56
print(promode_details.keys()) #None
print(promode_details.values()) #None
my_dict={'name':"shiv", 'age':45,'phone':"9800777", 'address':"kalash",'name':"om",'lord': 'om'}# duplicate key are not allowed
print(my_dict)#  keys are unique, but value can be duplicate
print(my_dict['name'])# om
print(my_dict.get('name'))# om

for key in my_dict.keys():
    print(key) # it will print all the keys
    print(my_dict[key]) # it will print all the values

for value in my_dict.values():
    print(value) # it will print all the values

for key,value in my_dict.items():
    print(key,value) # it will print all the key value pair
