text = (input("Enter your Text : ")).lower()
spam_words =["make a lot of money","Buy now","subscribe this","click this"]
for item in spam_words:
    if item in text:
        print("Spam detected.")
        break
else:
    print("No Spam detected")
