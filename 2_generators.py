def generator_function(value):
    for i in range(value):
        yield i

print("-> For cycle:")
for item in generator_function(7):
    print(item)

print("-> Usage of `next` function:")
gen = generator_function(3)
print(next(gen))
print(next(gen))
print(next(gen))
try:
    print(next(gen))
except StopIteration:
    print("handle `stop iteration` exception")

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print("-> Fibonacci in cycle:")
for x in fibon(5):
    print(x)

print("-> Fibonacci in cycle (again):")
for x in fibon(5):
    print(x)

print("-> Turn string to iterator:")
hello = "hello world"
hello_iterator = iter(hello)
print(next(hello_iterator))
print(next(hello_iterator))
print(next(hello_iterator))
print(next(hello_iterator))
print(next(hello_iterator))
