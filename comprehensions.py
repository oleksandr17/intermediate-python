#
print('-> List:')
multiples_list = [i for i in range(30) if i % 3 == 0]
print(multiples_list)

#
print('-> Set:')
multiples_set = {i for i in range(30) if i % 3 == 0}
print(multiples_set)

#
print('-> Dict:')
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {v: k for k, v in mcase.items()}
print(mcase_frequency)

#
print('-> Generator:')
multiples_gen = (i for i in range(30) if i % 3 == 0)
for i in multiples_gen:
    print(i)
