class Employee:
    #class attribute(static method like in java)
    city = "Banglore"
        
    def __init__(self, eid, ename, esalary, ecompany):
        self.eid = eid
        self.ename = ename
        self.esalary = esalary
        self.ecompany = ecompany
    
    def work(self):
        print(f"Employee {self.ename} with {self.eid} is working in {self.ecompany} Company, and is getting salary of RS{self.esalary}/-.")
        
    def Project(self, project):
        print(f"Employees are working on {project} project")
        
e1 = Employee(101, "Fayaz", 150000, "Kodnest")
e1.work()
e1.Project("BlockChain")
print(Employee.city)