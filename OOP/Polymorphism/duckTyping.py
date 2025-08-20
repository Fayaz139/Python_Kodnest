class Robo:
    def talk(self):
        print("The Robo is talking")
    def walk(self):
        print("The Robo is walking")
    def charge(self):
        print("The Robo is getting charged")

class FighterRobo (Robo):
    pass
        
class TeacherRobo (Robo):
    pass

class DriverRobo (Robo):
    pass

def access_robo(r):
    r.talk()
    r.walk()
    r.charge()

f = FighterRobo()
access_robo(f)
print()

t = TeacherRobo()
access_robo(t)
print()

d = DriverRobo()
access_robo(d)
