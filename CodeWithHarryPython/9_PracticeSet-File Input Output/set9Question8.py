with open("this.txt") as f:
    content = f.read()
    f.close()
with open("this-copy.txt","w") as f:
    f.write(content)
    f.close()