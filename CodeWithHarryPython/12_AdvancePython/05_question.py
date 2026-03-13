n = int(input("Enter a no. : "))
table_n = [i*n for i in range(1,11)]

with open("tables.txt","a") as f1:
    f1.writelines('\n')
    f1.writelines(str(table_n))