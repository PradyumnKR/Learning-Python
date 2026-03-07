#using set instead of list

dic = {}
print("Please type 'exit' in the name box if you want to exit the program.")
while True:
    name = input("Enter your name : ")
    if(name == "exit"):
        break
    lang = input("Enter you favourite Langugage : ")
    if(name in dic):
        dic[name].add(lang)
    else:
        dic[name] = {lang}
for key in dic:
    print(f"Name : {key}, Favourite Language : {dic[key]}")