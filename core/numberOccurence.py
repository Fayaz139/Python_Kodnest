numbers = list(map(int, input().split()))
count = {}
for i in numbers:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in count:
    print(i, "occurs", count[i], "time(s)")