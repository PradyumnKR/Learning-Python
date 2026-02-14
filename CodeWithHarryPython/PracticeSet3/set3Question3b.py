#Count the no. of groups of double spaces
a = input("Enter a string : ")
count = 0 
i =0
while (i<len(a)-1):
    if(a[i] == " " and a[i+1] == " "):
        while (i<len(a) and a[i]==" "):
            i = i+1
        count = count +1
    else:
        i = i+1

print(f"No. of groups of double space is {count}")