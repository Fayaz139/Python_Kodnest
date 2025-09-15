from functools import reduce
lst = [5,10,15,20,25]

# Square
def sqr(n):
    return n*n

square = map(sqr, lst)
print(f"The square of the list is: {list(square)}")

# Even Numbers
def even(n):
    return n%2 == 0

even_num = filter(even, lst)
print(f"The even numbers are: {list(even_num)}")

# Sum of lst
def sum_lst(a,b):
    return a+b

sum_num = reduce(sum_lst, lst)
print(f"The sum of the list is: {(sum_num)}")