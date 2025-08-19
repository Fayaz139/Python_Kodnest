class parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent constructor")

class child(parent):
    def __init__(self, n, age):
        super().__init__(n)
        self.age = age
        print(f"Child Constructor with age as {self.age}")
        print(f"Name of the person: {self.name}")
        print(f"Age of the person: {self.age}")
    
c = child("John", 22)