class Robo:
    def talk(self):
        print("The Robo is talking")
    def walk(self):
        print("The Robo is walking")
    def charge(self):
        print("The Robo is getting charged")

class FighterRobo (Robo):
    def talk(self):
        print("The FighterRobo is talking")
        
    def fight(self):
        print("Fights")
        
class TeacherRobo (Robo):
    def talk(self):
        print("The TeacherRobo is talking")
        
    def teach(self):
        print("Teaches")

class DriverRobo (Robo):
    def talk(self):
        print("The DriverRobo is talking")
        
    def drive(self):
        print("Drives")

def access_robo(r):
    r.talk()
    r.walk()
    r.charge()
    if isinstance(r, FighterRobo):
        r.fight()
    elif isinstance(r, TeacherRobo):
        r.teach()
    elif isinstance(r, DriverRobo):
        r.drive()

f = FighterRobo()
access_robo(f)
print()

t = TeacherRobo()
access_robo(t)
print()

d = DriverRobo()
access_robo(d)
