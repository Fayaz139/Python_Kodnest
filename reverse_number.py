num = int(input())
reversed_num = 0

n = num

while n > 0:
    digit = n % 10
    reversed_num = (reversed_num * 10) + digit
    n //= 10

print("The reversed number is", reversed_num)