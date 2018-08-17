def profile_global():
    global name
    global age
    name = 'Borat'
    age = 29

profile_global()
print('-> Profile global: {}, {}'.format(name, age))

###
def profile_tuple():
    return 'Borat', 29

profile_result = profile_tuple()
print('-> Profile tuple: {}, {}'.format(profile_result[0], profile_result[1]))

###
from collection import namedtuple
