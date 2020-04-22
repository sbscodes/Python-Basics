class ListIterator:
    def __init__(self,list):
        self.__list=list
        self.__index=-1

    def __iter__(self):
        return self
    def __next__(self):
        self.__index += 1
        return self.__list[self.__index]

a=[1,2,3,4,5]

Mylist=ListIterator(a)
it = iter(Mylist)
print(next(it))
print(next(it))