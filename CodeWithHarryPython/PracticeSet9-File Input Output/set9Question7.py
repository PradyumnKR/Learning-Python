with open("log.txt") as f:
    content = f.readlines()

for index,line in enumerate(content,start=1):
    if "python" in line:
        print(f"Python found at : {index} line.")
        break
else:
        print("Python is not present in the file.")

f.close() 

