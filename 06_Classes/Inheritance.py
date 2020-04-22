class shape:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return 2 *self.a * self.b

    def volume(self):
        return self.a * self.b

class circle(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        shape.volume(self)
        shape.area(self)

c=circle(20,30)
print(c.area())
print(c.volume())

