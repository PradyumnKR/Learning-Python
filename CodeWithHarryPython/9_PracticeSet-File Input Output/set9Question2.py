def game():
    hiscore = int(input("Enter you score : "))
    return hiscore

f = open("hiscore.txt","r+")
data = f.read()
hi_score_var = game()
if int(data)< hi_score_var:
    f.seek(0)
    f.write(str(hi_score_var))
    f.truncate()
f.close()