class Student:
    def __init__(self, name, roll, password):
        self.name = name #public
        self._roll = roll #protected
        self.__password = password #private
    
    #getters
    def get_password(self):
        return self.__password
    #setters
    def set_password(self,password):
        if len(password) >= 6:
            self.__password = password
        else:
            print("Password must be at least 6 characters long!")
    
    #getters
    def get_name(self):
        return self.name
    #setters
    def set_name(self, name):
        self.name = name
    
    #getters
    def get_roll(self):
        return self.roll
    #setters
    def set_roll(self, roll):
        self.roll = roll
    
s = Student("Fayaz", 81, "abc@123")
print(f"Name: {s.get_name()}")
print(f"Roll No: {s.get_roll()}")
# print(f"Password: {s.__password}") without getter and setter it gives error

print(f"Password: {s.get_password()}")
s.set_password("xyz13")

if s.get_password() == "******":
    print(f"Password: {s.get_password()}")