#args any number of arguments
print("shaiv","dev","raj")
# def sum3(a,b,c):
#     return a+b+c
# res=sum3(3,7,9)
# print(res)

def sum3(a=6,b=8,c=9):# default agr value is 6,8,9
    return a+b+c
res=sum3(3)# here a default value will be changed to 3
res1=sum3()
res2=sum3(3,10)
res3=sum3(56,78,90)
res4=sum3(3,80,)
res5=sum3(a=10,b=10,c=10)
print(res,res5,res4,res3,res2,res1)
# print(res1)
# print(res2)
# print(res3)
# print(res4)
# print(res5)

