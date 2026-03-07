censor_words = ["donkey","stupid","idiot"]

with open("quest5.txt","r") as f :
    content = f.read()
    f.close()
for word in censor_words:
    content = content.replace(word,"#"*len(word))

if(content !=""):
    with open("quest5.txt","w") as f:
        f.write(content)
        f.close()
else:
    print("Something went wrong!")
