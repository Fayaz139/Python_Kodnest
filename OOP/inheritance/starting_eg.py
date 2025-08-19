class SoftwareEngineer:
    eCompany = "ABC Company"
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept
    
    def softwareSkills(self):
        print("I have various Software skills")
        
    def intro(self):
        print("___Employee Details___")
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.dept}")
        print(f"Company: {Developer.eCompany}")

class Developer (SoftwareEngineer):
    def coding(self):
        print("I have Coding skills")


class Tester (SoftwareEngineer):
    def testing(self):
        print("I have Testing skills")


# Creating Developer objects
dev1 = Developer(201, "Alice", "Development")
dev1.intro()
dev1.softwareSkills()
dev1.coding()

print("\n")

dev2 = Developer(202, "Bob", "Development")
dev2.intro()
dev2.softwareSkills()
dev2.coding()

print("\n")

# Creating Tester objects
tester1 = Tester(301, "Charlie", "Testing")
tester1.intro()
tester1.softwareSkills()
tester1.testing()

print("\n")

tester2 = Tester(302, "David", "Testing")
tester2.intro()
tester2.softwareSkills()
tester2.testing()
 