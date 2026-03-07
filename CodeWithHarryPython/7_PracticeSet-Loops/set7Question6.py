# Factorial using while loop.
import sys
n = int(input("Enter num : "))
if(n<0):
    print("Invalid entry. Negative Numbers cannot be inputted.")
    sys.exit()
i =1 
fact = 1
while i<=n:
    fact = fact*i
    i=i+1
print(f"Factorial of {n} : {fact}")