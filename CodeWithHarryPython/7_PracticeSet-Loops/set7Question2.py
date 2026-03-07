# Greet all names in list that start with 'S'
#I can also make the data list a set for unique values and also make the content dynamic but its not required in the question. And I can also check for lowercase by using .lower() buts its also not explicitely required.
data = ["Saksham","Sanyam","Ramesh","Suresh","Girish"]
for name in data:
    if name.startswith("S"):
        print(f"Hello {name}! Greetings!!")
