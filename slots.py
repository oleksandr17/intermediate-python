print('-> Without slots:')

class WithoutSlots(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

a = WithoutSlots(1, 2)
a.c = 1
print(a.__dict__)

#
print('-> With slots:')

class WithSlots(object):
    __slots__ = ['a', 'b']
    def __init__(self, a, b):
        self.a = a
        self.b = b

b = WithSlots(1, 2)

try:
    b.c = 3
except AttributeError as e:
    print('Error: ', e)

try:
    print(b.__dict__)
except AttributeError as e:
    print('Error: ', e)
