a=20
b=10

try:
    c=a/b
    print("Divisiable")
except ZeroDivisionError:
    print("Number Not Divisible by Zero")

else:

    print("Divisiion of {0}/{1}={2}".format(a, b, a / b))
finally:print("--------END-------")