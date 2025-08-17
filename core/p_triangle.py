l = 5 #int(input())
b = 6 #int(input())

for i in range(1,l+1):
    for sp in range(1, b-i+1):
        print("-", end = "")
    for j in range(1, 2*i):
        print("*", end = "")
    print("")