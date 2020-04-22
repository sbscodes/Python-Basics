class Dog:
    kind = 'canine'  # Class variable shared by all instances.
    def __init__(self, name):
        self.name = name  # Instance variable unique to each instance.


fido = Dog('Fido')
print(fido.kind)
print(fido.name)
buddy = Dog('Buddy')
print(buddy.kind)
print(buddy.name)