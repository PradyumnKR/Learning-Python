class Employee:
    def __init__(self, name, basic, increment):
        self.name = name
        self.basic = basic
        self.increment = increment
        
    @property
    def salaryAfterIncrement(self):
        return self.basic * (1 + self.increment)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, val): # Added 'val' argument
        # We calculate the new increment based on the 'val' provided
        self.increment = (val / self.basic) - 1

em1 = Employee("Ramesh", 8000, 0.1)
print(f"Original Salary After Increment: {em1.salaryAfterIncrement}")

# This triggers the @setter
em1.salaryAfterIncrement = 10000 

print(f"New Increment calculated by setter: {em1.increment:.2f}") 
# .2f rounds it to 0.25