# Example of  Multi_level inheritance...
class Car:
    
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

class Toyota(Car): #Toyota extends Car

    def __init__(self, company_name = "Toyota"):
        self.company_name = company_name
    def company_info(self):
        print("Toyota is one of the most popular vehicle manufacturing company!!!")
    def get_company_name(self):
        return self.company_name
    

class Fortuner(Toyota):

    def __init__(self,name, color, type = "Manual"):
        self.name = name
        self.color = color
        self.type = type
    
    def show_specs(self):
        print("Name : ",self.name)
        print("Color : ",self.color)
        print("Type : ",self.type)
        print("Manufactured by : ",self.get_company_name)

f1 = Fortuner("Fortuner", "Black")
f1.show_specs()
f1.start()
f1.stop()

