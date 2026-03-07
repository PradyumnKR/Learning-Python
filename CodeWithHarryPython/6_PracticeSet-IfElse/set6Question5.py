data = []
choice ='y'
while choice.lower() == 'y':
    entry = input("Enter a name : ")
    data.append(entry.lower())
    choice = input("Do you want to enter more? (y/n): ")
    while choice.lower() not in ['y', 'n']:
        choice = input("Please enter 'y' or 'n': ")

name = input("Enter the name you want to check : ")
if name.lower() in data : 
    print("Name is present.")
else:
    print("Name is not present.")

    