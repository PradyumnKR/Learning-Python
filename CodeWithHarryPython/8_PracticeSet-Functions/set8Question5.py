# Write a function to print first n lines of the following pattern:
# ***
# **
# *
def inverted_half_pyramid(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("* ",end="")
        print()
inverted_half_pyramid(3)
