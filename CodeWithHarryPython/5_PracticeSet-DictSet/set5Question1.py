words = {"namaste": "hello", "shubh prabhat": "good morning", "shubh raatri": "good night"}

def lookUpAllWords(words):
    for key in words:
        print(f" {key} :{words[key]}")

def lookUpSingleWord(word):
    return words.get(word)

lookUpAllWords(words)

word = input("Enter the word you want to lookup : ").lower()
if(lookUpSingleWord(word) != None):
    print(f"Meaning of word {word} : {lookUpSingleWord(word)}")
else:
    print("Please Enter a Valid Word.")

