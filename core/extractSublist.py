l = list(map(int, input().split()))

i = int(input())
j = int(input())

lst = slice(i,j)
print("Extracted sublist:", l[lst])