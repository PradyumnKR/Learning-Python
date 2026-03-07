# Define a property that must have the same value for every class instance (object)
class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def getInfo(self):
        print(f"Color : {Vehicle.color} | Name : {self.name} | Speed : {self.max_speed} | Mileage : {self.mileage}")

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

school_bus = Bus("School Volvo",120,18)

toyota = Car("GXR7",200,16)
school_bus.getInfo()
toyota.getInfo()