#Rahul-> Python
#Rahul->Python X not allowed
#Rahul->Java allowed
dic = {}
while len(dic)<2:
    name = input("Enter your name : ")
    lang = input("Enter you favourite Langugage : ")
    if(name in dic):
        if(lang in dic[name]):
            print("Please enter a different Language, Same name entry already exists.")
        else:
            dic[name].append(lang)
    else:
        dic[name] = [lang]
for key in dic:
    print(f"Name : {key}, Favourite Language : {dic[key]}")