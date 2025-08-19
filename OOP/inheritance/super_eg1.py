class parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent constructor with name as {self.name}")

class child(parent):
    def __init__(self, n, age):
        super().__init__(n)
        self.age = age
        # print(f"Child Constructor with age as {self.age}")
    
c = child("John", 22)