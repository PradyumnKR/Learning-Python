f = open("test.txt","w")
data = "This is the written text"
f.write(data)
f.close

f = open("test.txt","r")
data = f.read()
print(data)
f.close