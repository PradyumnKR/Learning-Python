# Write a program to check whether a number is prime or not.
import math
# list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,1,4,6]
num = int(input("Enter a num : "))

def checkPrime(num):
    if(num <= 1):
        print("Not a prime.")
        return
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            print("Not a prime.")
            break
    else:
        print("Prime Number.")

# for i in list_of_primes:
#     checkPrime(i)
checkPrime(num)