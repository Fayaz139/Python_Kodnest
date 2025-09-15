# file = open("demo1.txt", "r")

# print(file.read())

# file.close()

with open("demo1.txt", "r") as file:
    text = file.read()
    print(text)
    
with open("demo1.txt", "r") as line:
    line1 = line.readline()
    line2 = line.readline()
    print(line1)
    print(line2)

with open("demo2.txt", "w") as line:
    l1 = line.write("Hello from Python")
    line.write("\nHello from java")
    line.write("\nHello from SQL")