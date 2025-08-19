class parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent constructor")
        
    def abc (self):
        print("Inside parent method")

class child(parent):
    def __init__(self, n, age):
        super().__init__(n)
        self.age = age
        
    def xyz(self):
        super().abc()
        print("Inside child method")
        print(f"Child Constructor with age as {self.age}")
        print(f"Name of the person: {self.name}")
        print(f"Age of the person: {self.age}")
    
c = child("John", 22)
c.xyz()