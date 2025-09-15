def test(func):
    def surpirse():
        func()
        print("surprise test!!")
        print("class finished")
    return surpirse

@test
def classes():
    print("class is going on.")
    
    
classes()