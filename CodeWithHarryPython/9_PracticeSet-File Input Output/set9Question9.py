with open("this.txt") as f :
    content1 = f.read()

with open("this-copy.txt") as f2:
    content2 = f2.read()

if content1 == content2:
    print("Both files have same content.")
else:
    print("Files have different content.")
f.close()
f2.close()