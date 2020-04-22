a=[1,2,3,4,5]

try:
    print(a[6])
except IndexError:
    print("Index Error Occurs")

finally:print("This block can execute anyway")