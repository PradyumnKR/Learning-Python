#Can we change contents of a list inside a set
#Ans - We cannot, since we cannot change values of set elements

s = {1, 2,True,[1,2]}
for item in s:
    if type(item) == 'list':
        item[0] = 3

#    s = {1, 2,True,[1,2]}
#         ^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'