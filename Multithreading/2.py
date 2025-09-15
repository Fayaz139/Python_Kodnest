import time, threading

print("VS Code Opened")

def coding():
    for i in range(5):
        print("coding...")
        time.sleep(1)

def errorCheck():
    for i in range(5):
        print("Checking errors...")
        time.sleep(1)

def autoSave():
    for i in range(5):
        print("Saving...")
        time.sleep(1)


t1 = threading.Thread(target=coding)
t2 = threading.Thread(target=errorCheck)
t3 = threading.Thread(target=autoSave)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("VS Code Closed")