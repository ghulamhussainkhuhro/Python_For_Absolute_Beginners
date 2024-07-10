# Inheritance in python
"""
When one class(Child or drived) class drives the properties and methods of another class (parent or base )

"""

# Example of Single level inheritance...
class Car:
    
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class Toyota(Car): #Toyota extends Car

    def __init__(self, name):
        self.name = name
    
car1 = Toyota("Fortuner")
car1.start()
car1.stop()
car2 = Toyota("Corolla")
car2.start()
car2.stop()