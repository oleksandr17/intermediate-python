from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from enum import Enum

print('-> defaultdict:')

colours = [
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
]

favourite_colours = defaultdict(list)
for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

#
print('-> Counter:')

favs = Counter(name for name, colour in colours)
print(favs)

#
print('-> OrderedDict:')

colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)

#
print('-> deque:')

d = deque()

d.append('1')
d.append('2')
d.append('3')

print(d)
print(len(d))
print(d[0])
print(d[-1])

d.popleft()
d.pop()
print(d)

d.extendleft([1])
d.extend([3])
print(d)

#
print('-> namedtuple:')

man = ('Ali', 30)
print(man[0], man[1])

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry)
print(perry.name)
print(perry[0])

#
print('-> enum:')

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9

    kitten = 1
    puppy = 2

print(Species(1))
print(Species['cat'])
print(Species.cat)

animal = Species.cat
print('Is cat: ', animal == Species.cat)
print('Is dog: ', animal == Species.dog)
