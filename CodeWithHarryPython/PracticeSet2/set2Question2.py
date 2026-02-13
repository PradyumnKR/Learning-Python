num = int(input("Enter a number:"))
z = int(input("Enter number to divide by : "))

try :
    if(z == 0):
        raise ZeroDivisionError 
    remainder = num % z
    print("The remainder is :",remainder)
except ZeroDivisionError:
    print("You cannot divide by zero")