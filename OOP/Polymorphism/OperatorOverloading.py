class Circle:
    def __init__(self, rad):
        self.rad = rad
    def __add__(self, other):
        return (self.rad + other.rad)

c1 = Circle(10)
print(f"area = {3.14*c1.rad*c1.rad}")

c2 = Circle(12.5)
print(f"area = {3.14*c2.rad*c2.rad}")

print(f"Sum of radius: {c1+c2}")