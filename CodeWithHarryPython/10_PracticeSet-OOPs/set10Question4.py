#Making a calculator
import math
class Calculator:
    def __init__(self,num):
        self.num = num
    @staticmethod
    def greet():
        print("Hello User!")
    def square(self):
        return self.num*self.num
 
    def squareRoot(self):
        return math.sqrt(self.num)
   
    def cube(self):
        return self.num*self.num*self.num
c1 =Calculator(3)
print(c1.greet())
print(f"Square of {3} is : {c1.square()}")
print(f"Square root of {3} is : {c1.squareRoot()}")
print(f"Cube of {3} is : {c1.cube()}")

    


    