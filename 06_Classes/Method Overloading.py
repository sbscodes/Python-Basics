class Overload:

    def Print(self,name=None):
        if name==None:
            print("Called Without parameter")
        else:
            print("\nCalled with parameter "+name)

d=Overload()
d.Print()
d.Print("Rahul")