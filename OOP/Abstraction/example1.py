from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using CreditCard")
        
p1 = UPI()
p1.pay(500)

p2 = CreditCard()
p2.pay(1000)