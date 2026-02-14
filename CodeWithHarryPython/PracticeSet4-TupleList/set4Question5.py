a = (7,0,8,0,0,9)

#loop method 
def loopMethod(a):
    count = 0
    for num in a : 
        if num == 0:
            count = count +1
    return count

#tuple function method 

def funcMethod(a):
    countt = a.count(0)
    return countt

print(f"Count using loop : {loopMethod(a)}")
print(f"Count using the inbuilt count func of tuple : {funcMethod(a)}")