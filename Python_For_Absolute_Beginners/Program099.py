# Abstraction in OOP: Hiding the implementaion details of the class and only showing the essential featurea to user

class Car:

    def __init__(self) -> None:
        print("Car's iginition is on but is not moving...")
        # These 3 attributes are in  abtraction i.e person will only get the message 
        # that car started moving or stopped but how it started or 
        # stopped (It's implemmentaion is hidden)
        self.clutch = False
        self.brk = False
        self.acc = False

    def move(self):
        self.clutch = True
        self.acc = True
        print("Car started moving forward!!!")
    
    def stop(self):
        self.clutch = False
        self.acc = False
        self.brk = True
        print("Car stopped moving...")

car1 = Car()
car1.move()
car1.stop()
    
