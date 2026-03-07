# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def getInfo(self):
        print(f"Max Speed : {self.max_speed}")
        print(f"Mileage : {self.mileage}")

car1 = Vehicle("200kmph",38)
car1.getInfo()