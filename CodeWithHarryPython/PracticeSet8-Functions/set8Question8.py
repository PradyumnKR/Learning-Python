#Using function print multiplicatin table of a given number.
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter the no. whose table you want : "))

table(n)