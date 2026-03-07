#Greatest of 4 no. inserted by client 
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
d = int(input("Enter d : "))
#dictionary for keeping track of variable using max()
data = {
    "a":a,
    "b":b,
    "c":c,
    "d":d
}
def ifElseLadder(a,b,c,d):
    if( a > b):
        if(a > c):
            if(a>d):
                return {"a":a}
            else:
                return {"d":d}
        if(c>d):
            return {"c":c}
        else:
            return {"d":d}
    else:
        if(b>c):
            if(b>d):
                return {"b":b}
            else:
                return {"d":d}
        else:
            if ( c>d):
                return {"c":c}
            else:
                return {"d":d}
def usingMax(a,b,c,d):
    max_var = max(data,key=data.get)
    max_value = data[max_var]
    return {max_var:max_value}
    
    return 
# print(f"Greatest of 4 : {ifElseLadder(a,b,c,d)}")
print(f"Greatest of 4 : {usingMax(a,b,c,d)}")

