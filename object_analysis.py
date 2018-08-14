print(dir(''))

print(dir())

print(type(''))
print(type([]))
print(type({}))
print(type(3))
print(type(dict))
print(type(int))

name = ''
name_2 = name
print(id(name))
print(id(name_2))

import inspect
print(inspect.getmembers(str))