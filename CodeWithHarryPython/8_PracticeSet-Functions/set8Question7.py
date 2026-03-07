# Remove a given word from a list and strip it at the same time.

data =["  apple  ", "banana", " mango ", "banana  "]

def remove_and_strip(word_to_remove):
    global data # Tell the function to modify the 'data' outside
    
    # 1. Strip all items first
    # 2. Keep the item ONLY if it's not the word we want to remove
    data = [item.strip() for item in data if item.strip() != word_to_remove]
    print(f"All instances of '{word_to_remove}' removed and list stripped.")

word = input("Enter the word you want to remove: ")
remove_and_strip(word)


choice = input("Do you want to see the new list ?(y/n): ").lower()
while choice not in ['y','n']:
    choice = input("Please enter a valid choice (y/n) : ")
if(choice == 'y'):
    print(f"New List : {data}")



            

