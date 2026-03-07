import os
os.mkdir("tables")
for i in range(2,21):
    file_name = f"{i}_table.txt"
    with open(os.path.join("tables", file_name), "w") as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}\n")
    
