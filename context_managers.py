import random
from contextlib import contextmanager


# CLASS
class RandomContextManager(object):
        def __init__(self):
            self.value = random.randint(1,99)
        def __enter__(self):
            print('Enter')
            return self.value
        def __exit__(self, type, value, traceback):
            print('Exit')

print('-> Random:')
with RandomContextManager() as random_value:
    print('Value: {}'.format(random_value))

# EXCEPTION HANDLING
class DummyContextManager(object):
        def __init__(self):
            self.value = 'dummy'
        def __enter__(self):
            print('Enter')
            return self.value
        def __exit__(self, type, value, traceback):
            print('Exit')
            if value:
                print('Handle exception')
                return True

print('-> Dummy:')
with DummyContextManager() as dummy_value:
    print('Value: {}'.format(dummy_value))
    raise Exception('Dummy')

# GENERATOR
@contextmanager
def static_value():
    print('Enter')
    yield 42
    print('Exit')

print('-> Static:')
with static_value() as value:
    print('Value: {}'.format(value))
