class balanceException(Exception):
    pass

class bankaccount:
    def __init__(self,depammount,name):
        self.balance = depammount
        self.name = name
        print(f"an account has been created with '{name}' as name\nbalance =${depammount:.3f}")

    def getbalance(self):
        print(f"the '{self.name}' has ${self.balance:.3f}")
    
    def depo(self,amount):
        self.balance = self.balance + amount
        print(f"depost is succesful!")
        self.getbalance()

    def viabletrans(self,amount):
        if self.balance >= amount:
            return
        else:
            raise balanceException(f"sorry, the acc '{self.name}' has $'{self.balance}' ")
    
    def withdraw(self,amount):
        try :
            self.viabletrans(amount)
            self.balance = self.balance - amount
            print("withdraw complete")
            self.getbalance()
        except balanceException as error:
            print(f"withdraw interrupted : {error}")