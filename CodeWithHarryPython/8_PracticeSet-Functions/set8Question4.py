# Recursive function to calculate sum of first n natural numbers
def sum_of_first_n_natural_numbers(n):
    if(n==1):
        return 1
    return n + sum_of_first_n_natural_numbers(n-1)

n = int(input("Please enter n : "))
if(n<1):
    print("invalid input.")
else:
    print(f"Sum of {n} first natural numbers : {sum_of_first_n_natural_numbers(n)}")