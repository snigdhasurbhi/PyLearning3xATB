#Banch of character
#string
#"", '', """
name= "harry"
name1= 'harry'
name2= """harry is goood person ........
....
............................
................................
...........................
""" #multiline string for long string

print(name)
print(name1)
print(name2)
#difference between single and double quotes
#single quotes are used for single word
#doubt
dir= r'cd:\e\dou\my\mypc'
#RAW String we had to use r before the string to ignore the escape character
dir1=  r"cd:\e\dou\my\mypc\somedr"
print(dir)
print(dir1)
#Format of string
name= "harry"
age= 20
print("hello " + name + " your age is " + str(age))
#{} is the place holder
print("hello {} your age is {}".format(name, age))
print(name,age)
#f string is the latest version of string formatting
#f string is used to format the string
print(f"hello {name} your age is {age}")



