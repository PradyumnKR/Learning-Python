fruits = []
for i in range(7):
    fruit = input("Enter the name of a fruit : ")
    fruits.append(fruit)
tupleOfFruits = tuple(fruits)
print(f"The tuple of fruits is : {tupleOfFruits}")