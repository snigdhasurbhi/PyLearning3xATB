# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

#1st type
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1): #if stop will be n then it would went till 6 only default n-1
  fact = fact * i
  print(f"Current value of fact is {fact}")


#2nd type
n1 = int(input("Enter a number: "))
def fact(n1):
   if n1==1:
       return 1
   else:
       return n1*fact(n1-1)
print(fact(n1))
