#when one class is derived from two parent calsses is called as
#multiple inheritance

class Name:
    name=" "
    def __init__(self,name):
        self.name = name
    def PrintName(self):
        print("Name is "+str(self.name))


class Id:
    id1=0
    def __init__(self , id1):
        self.id1 = id1
    def Printid(self):
        print(self.id1)

class Employee(Name,Id):

    def __init__(self, name ,id1):
        super().__init__(name)
        super().__init__(id1)

    def PrintDet(self):
        super().PrintName()
        super().Printid()


d=Employee(50,"Rahul")
d.PrintDet()