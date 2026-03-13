a = int(input("Enter a : "))
b = int(input("Enter b : "))

try : 
    ans = a/b
    print(ans)
except ZeroDivisionError:
    print("We cannot divide by 0. Choose something else for denominator.")