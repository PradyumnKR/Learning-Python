dic = {}
for i in range(5):
    name = input("Enter your name : ")
    lang = input("Enter you favourite Langugage : ")
    dic[name] = lang
for key in dic:
    print(f"Name : {key}, Favourite Language : {dic[key]}")