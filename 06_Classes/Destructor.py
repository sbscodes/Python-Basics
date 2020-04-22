class Des:
    def __init__(self,value,name):
        self.name=name
        self.value=value

    def __del__(self):
        class_name=self.__class__.__name__
        print (class_name,"Destroyed")

d1=Des(30,"goods")
del d1 #del function is use to destruct the class constructor object