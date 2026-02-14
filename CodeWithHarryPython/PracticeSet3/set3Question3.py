# a = "this a  string"
# if("  " in a):
#     print("There is a double space in the string")

#Program to find no. of double spaces present in the string
a = input("Enter a string : ")
count = 0 
for i in range(len(a)-1):
    if(a[i]==" " and a[i+1]==" "):
        count = count + 1
print(f"The number of double spaces present in the given string is {count}")
