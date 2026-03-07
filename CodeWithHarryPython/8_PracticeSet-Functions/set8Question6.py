# Convert inches to centimeters using function.
def inches_to_centimeter(inches):
    return inches*2.54
inches = float(input("Enter inches : "))
print(f"Inches -> CM : {inches_to_centimeter(inches)} cm")