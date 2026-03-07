# Find sum of first n natural numbers using while loop.
import sys
n = int(input("Enter the which upto you want the sum : "))
if n<0:
    print("Invalid entry.")
    sys.exit()
#formula method 
# sum = (n*(n+1))/2
# print(int(sum))
sum = 0 
i =1
while i<=n:
    sum = sum+i
    i=i+1
print(f"Sum of {n} Natural numbers is : {sum}")