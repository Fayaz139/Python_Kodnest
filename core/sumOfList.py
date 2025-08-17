l = list(map(int, input().split()))

sum = 0
for i in l:
    sum+=i

avg= sum/len(l)

print("The average of the list is:", avg)