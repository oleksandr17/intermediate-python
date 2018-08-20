fruits = ['apple', 'banana', 'grapes', 'pear']

print('-> Full list:')
for counter, value in enumerate(fruits):
    print('{}) {}'.format(counter, value))

print('-> Counter offset:')
for counter, value in enumerate(fruits, 1):
    print('{}) {}'.format(counter, value))
