try:
    with open("1.txt") as f1, open("2.txt") as f2, open("3.txt") as f3:
        f1.write("Hello World")
        data = f3.read()
        print(data)
except FileNotFoundError:
    print("File Not Found")
except Exception as e:
    print(e)


    