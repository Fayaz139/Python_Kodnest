n = int(input())
num = n
f = False
while n > 0:
    dig = n % 10
    if dig % 2 == 0:
        print(f"The last even digit in {num} is {dig}")
        f = True
        break
    n = n // 10

if f == False:
    print("No even digit found.")