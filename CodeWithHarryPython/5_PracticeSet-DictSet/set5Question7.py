#What would happen if the names of 2 friends is same in the above question ?
#Ans : Since keys in dictionary are unique, if names of two friends is same then dictionary will overwrite the value of first friend and the data would be dost. So ideally no name should ever repeat.

dic = {}
while len(dic)<4:
    name = input("Enter your name : ")
   
    if(name in dic):
        print("Please enter a different name, Same name entry already exits.")
    else:
        lang = input("Enter you favourite Langugage : ")
        dic[name] = lang
for key in dic:
    print(f"Name : {key}, Favourite Language : {dic[key]}")