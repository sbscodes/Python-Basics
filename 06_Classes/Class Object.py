class info:
    msg="This is class object"
    def empty(self):
        pass

i=info()#here i is the object of class
i.msg="hello"
print(i.msg)


class ComplexNumber:

    real = 0
    """these both are class objects which change may occure in change in other 
    functions or variables"""
    imaginary = 0

    def get_real(self):
        """Return real part of complex number."""
        return self.real
    def get_imaginary(self):
        """Return imaginary part of complex number."""
        return self.imaginary
c=ComplexNumber()
c.real=10
c.imaginary=20
print(c.real)
print(c.imaginary)
print(c.get_real())
print(c.get_imaginary())