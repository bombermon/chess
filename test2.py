class b(object):
    def __init__(self, a):
        self.s = 1
        self.chell = a

class a(object):
    def __init__(self):
        self.s = 2
        self.chell = b(self)

d = a()
print(d.s, d.chell.s, d.chell.chell.chell.s)
