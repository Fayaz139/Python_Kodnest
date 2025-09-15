from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def walk(sel):
        pass
    @abstractmethod
    def talk(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
    
class Dog(Animal):
    def sleep(self):
        print("Dog is sleeping")
        
    def walk(self):
        print("Dog is walking")
    
    def talk(self):
        print("Dog is talking")
        
d = Dog()
d.walk()