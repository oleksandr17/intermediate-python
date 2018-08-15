# Single exception
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('IOError: {}'.format(e))

# Multiple exceptions
print("-------------------------------------")
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print('IOError or EOFError: {}'.format(e))

print("-------------------------------------")
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('IOError: {}'.format(e))
except EOFError as e:
    print('EOFError: {}'.format(e))

# All exceptions
print("-------------------------------------")
try:
    file = open('test.txt', 'rb')
except Exception as e:
    print('Exception: {}'.format(e))

# Finally
print("-------------------------------------")
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('IOError: {}'.format(e))
finally:
    print("Finally block")

# try/else
print("-------------------------------------")
try:
    print('Exception free block')
except Exception:
    print('Exception')
else:
    print('Else block, called in case there is no exception')
finally:
    print('Finally block, called anyway')
