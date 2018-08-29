class WithoutSlots(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

a = WithoutSlots('no slots', 1)


class WithSlots(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

b = WithoutSlots('slots', 2)
