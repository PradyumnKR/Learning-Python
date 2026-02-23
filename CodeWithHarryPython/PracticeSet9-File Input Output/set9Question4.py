censor = "#####"
f = open("quest4.txt","r+")
content = f.read().lower()
content= content.replace('donkey',censor)
f.seek(0)
f.write(content)
f.truncate()
print(content)
# for i in range(len(content)):
#     if content[i]== "d":
#         temp = content[i:i+5]
#         if temp == "donkey":
            

