#factorial
import math
n=5
fac=1
#result =math.fac(5)
#print(result)
# for i in range(1,n+1): #range is a list item
#     fac=fac*i
#     print(fac)
while(n>0):
    fac=fac*n
    n=n-1
    print(fac)