import time, threading

def task():
    while True:
        print("Background task running")
        time.sleep(1)

print("Coding starts.")

t = threading.Thread(target=task)
t.daemon = True
t.start()

for i in range(5):
    print("Coding")
    time.sleep(1)

print("Main program ends.")