#    *
#   ***
#  *****
# *******
n = int(input("Enter n : "))

for i in range(n):
    # Loop for spaces
    for j in range(n - i - 1):
        print(" ", end="")
        
    # Loop for stars
    for k in range(2 * i + 1):
        print("*", end="")
        
    # Move to the next line
    print()