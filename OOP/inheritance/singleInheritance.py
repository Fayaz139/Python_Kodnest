# Base Class
class Vehicle:
    def start(self):
        print("The vehicle is starting.")

# Subclass
class Car(Vehicle):
    def honk(self):
        print("The car is honking. Beep beep!")

# Creating Instance
car1 = Car()
car1.start()
car1.honk()