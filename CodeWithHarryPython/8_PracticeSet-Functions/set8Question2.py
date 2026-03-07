# Convert Celsius to Fahrenheit using function.
def CeltoFaren(C):
    return (C*(9/5)+32)
def FarentoCel(F):
    return ((F-32)*(5/9))

C = float(input("Enter the Celcius temperature you need in Fareheit : "))
F = float(input("Enter the Farenheit temperature you need in Celcius : "))

print(f"Celcius to Farenheit : {CeltoFaren(C)}")
print(f"Farenheit to Celcius : {FarentoCel(F)}")