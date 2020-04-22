def f(food: str, work: str = 'gyming') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", food,work)
    print(food + ' and ' + work)

f('banana','Eating')
