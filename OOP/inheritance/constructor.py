class parent:
    def __init__(self):
        print("Parent constructor")

class child1 (parent):
    pass

class child2(parent):
    def __init__(self):
        print("Child Constructor")
    
c1 = child1()
c2 = child2()