# No duplicate names (case insensitive)
# No duplicate languages (case insensitive)
# Preserve original formatting for printing

UserDictionary = {}  # Dictionary to store user data
print("Please type 'exit' in the name box if you want to exit the program.")

while True:
    display_name = input("Enter your name : ")
    if display_name.lower() == "exit":
        break

    display_lang = input("Enter your favourite Language : ")

    name_key = display_name.lower()
    lang_key = display_lang.lower()

    # If name not already present
    if name_key not in UserDictionary:
        UserDictionary[name_key] = {
            "display_name": display_name,
            "display_language": {display_lang},   # original format
            "languages": {lang_key}               # lowercase for checking duplicates
        }
    else:
        # Check duplicate language (case insensitive)
        if lang_key in UserDictionary[name_key]["languages"]:
            print("Duplicate Entries not Allowed.")
        else:
            UserDictionary[name_key]["display_language"].add(display_lang)
            UserDictionary[name_key]["languages"].add(lang_key)

# Printing results
for key in UserDictionary:
    print(f"Name : {UserDictionary[key]['display_name']}, Favourite Language : {UserDictionary[key]['display_language']}")
