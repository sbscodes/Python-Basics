# def OuterFucntion(name,age):
#     def Innerfunction():
#         print("Name is {0} and age is {1}".format(name,age))
#     return Innerfunction()
#
# OuterFucntion("Tom",20)

"""
Above the function is the simple function which has one innerfunction
but when we delete outer function the inner function has no existance of 
data values
so therfore we use the clouser function as follows
"""
def OuterFucntion(name,age):
    def Innerfunction():
        print("Name is {0} and age is {1}".format(name,age))
    return Innerfunction

d = OuterFucntion("Tom",20)
del OuterFucntion
d()

