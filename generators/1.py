def generator_function():
    yield 11
    yield 22
    yield 33
    yield 44

a = generator_function()
print(next(a))
print(next(a))
print(next(a))
print(next(a))