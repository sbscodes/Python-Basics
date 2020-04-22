class CoffeToHot(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CoffeToCold(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Coffeshop:
    def __init__(self, temprature):
        self.__temprature = temprature

    def DrinnkCoffe(self):
        if self.__temprature >= 85:
            raise CoffeToHot('Coffe Temp is :'+ str(self.__temprature))
        if self.__temprature <  0:
            raise CoffeToCold('Coffe Temp is :' + str(self.__temprature))
        if self.__temprature == 50:
            print('Coffe Temp is :' + str(self.__temprature))
            print("it is ok to drink")

cf=Coffeshop(50)
cf.DrinnkCoffe()
