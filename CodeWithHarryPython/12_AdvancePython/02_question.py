myList = [1,2,4,5,6,3,5,2]

for index,value in enumerate(myList,start=1):
    if index in [3,5,7]:
        print(value)