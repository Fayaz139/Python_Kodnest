lst = [5,10,15,20,25]

#square
squares = []
for i in lst:
    squares.append(i*i)
print(squares)


#find even numbers

for i in lst:
    if i % 2 == 0:
        print(i)
#sum of all numbers
sum = 0
for i in lst:
    sum = sum + i 
print(sum)