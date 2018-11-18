# Singleton/BorgSingleton.py
# Alex Martelli's 'Borg'

class Borg(object):
    class __Borg:
        def __init__(self):
            self.speak = None
        def __str__(self):
            return repr(self) + self.speak

    instance = None
    def __new__(cls):
        if not Borg.instance:
            Borg.instance = Borg.__Borg()
        return Borg.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)

x = Borg()
x.speak = 'We are Borg'
print(x)

y = Borg()
y.speak = 'Resistance is futile'
print(y)

print(x)
print(y)
