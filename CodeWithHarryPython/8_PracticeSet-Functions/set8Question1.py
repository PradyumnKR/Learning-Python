# Write a program using functions to find greatest of three numbers.
def greatest(a,b,c):
    return max(a,b,c)
a = int(input("Enter num a : "))
b = int(input("Enter num b : "))
c = int(input("Enter num c : "))
print(f"Greatest of the three numbers is {greatest(a,b,c)}")