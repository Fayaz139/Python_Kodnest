n = int(input())
sum = 0

while n > 0:
    dig = n % 10
    sum += dig
    n //= 10

print("The sum of the digits is",sum)