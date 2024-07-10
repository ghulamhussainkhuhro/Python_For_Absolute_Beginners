class Car:

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class Toyota(Car):

    def __init__(self,name, type):
        super().__init__(type)
        self.name = name
        super().start()
        super().stop

    def show_data(self):
        print("Name : ",self.name)
        print("Type : ",self.type)
car1 = Toyota("Fortuner","Manual")
car1.show_data()