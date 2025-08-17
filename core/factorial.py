sum = 1
n = int(input())

for i in range(n,1,-1):
    sum *= i
print("The factorial of",n,"is",sum)