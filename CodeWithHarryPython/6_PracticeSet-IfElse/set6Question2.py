sub1 = float(input("Enter Marks of Subject 1 : "))
sub2 = float(input("Enter Marks of Subject 2 : "))
sub3 = float(input("Enter Marks of Subject 3 : "))

tot = (sub1+sub2+sub3)/3
if(tot>=40 and ((sub1>=33) and (sub2>=33) and (sub3>=33))):
    print("You Passed!")
else:
    print("You Failed.")
