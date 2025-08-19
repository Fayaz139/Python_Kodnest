#This type of inheritance is not possible in java!!
#Multiple Inheritance

# Base Class 1
class Electric:
    def charge(self):
        print("The vehicle is charging.")

# Base Class 2
class Engine:
    def fuel(self):
        print("The vehicle is refueling.")

# Subclass inheriting from both
class HybridCar(Electric, Engine):
    def drive(self):
        print("The hybrid car is driving.")

# Creating Instance
hybrid_car = HybridCar()
hybrid_car.charge()  # Output: The vehicle is charging.
hybrid_car.fuel()    # Output: The vehicle is refueling.
hybrid_car.drive()   # Output: The hybrid car is driving.