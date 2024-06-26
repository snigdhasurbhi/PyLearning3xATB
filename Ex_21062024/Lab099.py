#Dictonary
#Key value pair, key can be string or integer
#dict is an unorder collection of key value pair, it is mutable in nature
#Creating a dictonary
a={"name":"Shiv","Age":100,"Roll no":250, "address" : "kashi"}# key is name and value is shiv
my_dict={
    "name":"Aman",
    "Age":19,
    "Roll no":25
}# key is name and value is aman

print(a)
print(my_dict)
#Accessing a value
print(a["name"])#this will print shiv
print(my_dict["name"])#this will print aman
#Adding a new key value pair
a["address"]="kalash"
print(a)
#Updating a value
a["name"]="Shivam"
phone_book=dict(name="shiv",age=45,phone="9800777")
#this is another way to create a dictonary
print(phone_book)



