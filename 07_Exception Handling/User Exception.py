class NoMoney(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Bank:

    def withdraw(self):
        a = 500
        c=int(input("Enter Amount to Withdraw"))
        try:
            if(c>=500):
                raise NoMoney("Extra amount try to withdraw")
        except NoMoney as e:
            print(e)
        else:
            a = a - c
            print("Withdraw Succesful %d" % a)
b=Bank()
b.withdraw()