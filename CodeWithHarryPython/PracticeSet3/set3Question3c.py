#using regular expressions to find the count of double spaces 
import re 
a = input("Enter your string : ")
count = re.findall(r" {2,}",a)
print(len(count))