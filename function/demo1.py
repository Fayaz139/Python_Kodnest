# NO PARAMETER + NO RETURN
def greet():
    print("Have a good day!!")

greet()

# PARAMETER + NO RETURN
def add(a , b):
    sum = (a+b)
    print("Sum =",sum)

add(10,20)

# NO PARAMETER + RETURN
def calc_SI():
    p = 1000
    t = 3
    r = 12.5
    si = (p*t*r)/100
    return si

res = calc_SI()
print("SI =",res)

# PARAMETER + RETURN
def find_cube(n):
    cube = n ** 3
    return cube

result = find_cube(5)
print("Cube =",result)