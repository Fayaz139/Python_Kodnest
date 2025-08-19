class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def displayVehicle(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        
class Engine:
    def __init__(self, type):
        self.type = type
        
    def displayEngine(self):
        print(f"Engine Type: {self.type}")

class Car(Vehicle, Engine):
    def __init__(self, brand, model, type):
        Vehicle.__init__(self, brand, model)
        Engine.__init__(self, type)
    
    def displayCar(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Engine Type: {self.type}")

class ElectricCar(Car):
    def __init__(self, brand, model, type, batteryCapacity):
        Vehicle.__init__(self, brand, model)
        Engine.__init__(self, type)
        self.batteryCapacity = batteryCapacity
    
    def displayElectricCar(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Engine Type: {self.type}")
        print(f"Battery Capacity: {self.batteryCapacity}")

a = input()
b = input()
c = input()
d = input()

ca = ElectricCar(a, b, c, d)
ca.displayElectricCar()