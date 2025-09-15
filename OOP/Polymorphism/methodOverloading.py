class MathOperation:
    def add(self, *args):
        print(f"sum: {sum(args)}")

a = MathOperation()
a.add(10,20)
a.add(20,30,40,50)
a.add(1,1,2,3,4,5,6)