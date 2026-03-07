f = open("poems.txt")
data = f.read().lower()
if "twinkle" in data:
    print("twinkle present in data.")
else:
    print("twinkle not present in the file.")
f.close()