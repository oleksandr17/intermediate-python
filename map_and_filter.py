print('-> Map:')

print('Pass list of numbers:')
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

print('Pass list of functions:')
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

#
print('-> Filter:')
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# 
from functools import reduce

print('-> Reduce:')
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
