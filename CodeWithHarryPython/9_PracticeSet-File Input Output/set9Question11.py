import os
# with open("quest11.txt","w") as f :
#     f.write("This is a demo content.")
# f.close()

try:
    os.rename('quest11.txt', 'this_file_was_rename_by_Python.txt')
    print("Success! File renamed.")
except FileNotFoundError:
    print("Error: The source file was not found.")
except PermissionError:
    print("Error: You don't have permission to rename this file.")