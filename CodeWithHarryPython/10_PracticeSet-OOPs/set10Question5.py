class train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}.")
        print(f"The fare of the train is {self.fare}.")
        print(f"The number of seats available in the train are {self.seats}.")

    def bookTicket(self):
        if self.seats>0:
            print("Your ticket has been booked!")
            self.seats = self.seats - 1
        else:
            print("Sorry, no seats available!")

    def cancelTicket(self):
        print("Your ticket has been cancelled!")
        self.seats = self.seats + 1