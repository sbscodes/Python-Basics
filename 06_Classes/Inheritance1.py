class Employee:
    name=" "
    id=0
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def PrintDetails(self):
        print("Employee Name is" ,self.name)
        print("Employee id is" ,self.id)

class Manager(Employee):
    mid=0
    def __init__(self,mid):
        super().__init__(name,id)
        self.mid=mid
    def PrintDetails(self):
        super().PrintDetails()
        print("Manager id is" , self.mid)


if __name__=='__main__':
    print("Enter Employee Details")
    name = str(input("Enter Employee Name"))
    id = int(input("Enter Employee id"))
    mid = int(input("Enter Employee mid"))

    m = Employee(name,id)
    m.PrintDetails()