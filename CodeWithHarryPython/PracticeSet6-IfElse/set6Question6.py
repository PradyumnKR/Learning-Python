marks = int(input("Enter your marks : "))
if(marks<0 and marks>100):
    print("Invalid entry.")
elif(marks>=90):
    print("EX")
elif(marks>=80):
    print("A")
elif(marks>=70):
    print("B")
elif(marks>=60):
    print("C")
elif(marks>=50):
    print("D")
else:
    print("F")