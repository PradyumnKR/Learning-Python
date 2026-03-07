
name = input("Enter your name : ")
position= input("Enter the position you got selected for : ")
date = input("Enter the date of joining : ")
letter = f'''
Dear {name},
You are selected for the position of {position} in our company. We are looking forward to working with you. On Date {date}'''
print(letter)