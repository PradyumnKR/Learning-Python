#MY CODE--------------------------------------
# class programmers:
#     company = "Microsoft"
#     def __init__(self):
#         self.name = input("Enter the name of the programmer : ")

#         self.role =input("Enter the role of the programmer : ")
#         self.salary = int(input("Enter the salary of the programmer : "))
#         print("Details acquired. Created object...")
#     def getDetails(self):
#         print(f"The name of the programmer is {self.name}")
#         print(f"The role of the programmer is {self.role}")
#         print(f"The salary of the programmer is {self.salary}")
#         print(f"The company of the programmer is {programmers.company}")

# p1 = programmers()
# p2 =programmers()
# p1.getDetails()
# p2.getDetails()


#--------------------REFINED CODE----------------------------------------
class Programmer:
    company = "Microsoft" # Class Attribute

    def __init__(self, name, role, salary):
        # Instance Attributes
        self.name = name
        self.role = role
        self.salary = salary

    def get_details(self):
        print(f"Name: {self.name} | Role: {self.role} | Salary: {self.salary} | Company: {self.company}")

# Creating objects by passing arguments
p1 = Programmer("Alice", "SDE 1", 120000)
p2 = Programmer("Bob", "Senior Architect", 250000)

p1.get_details()
p2.get_details()