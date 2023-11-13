class balanceFlag(Exception):
    pass
    
class BankAccount:
    #def __init__(self,InitialDeposit, AccName):
    def __init__(self):
        self.name = AccName = input('Enter your account name')
        self.balance = InitialDeposit = input('Enter your initial deposit:')
        self.balance = float(self.balance)
        print(f"\nAccount {self.name} has been created.\n Your Balance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nYour deposit is complete")
        self.getBalance()
    
    def viableTransaction (self, amount):
        if self.balance >= amount:
            return
        else:
            raise balanceFlag (f"Your account only has ${self.balance:.2f}, you are missing ${amount-self.balance:.2f} to complete the process")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("Your withdraw was complete")
            
        except balanceFlag as error:
            print(f"Can't withdraw, {error}.")
    
    def transfer(self, amount, account):
        try:
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer Complete')
        except balanceFlag as error:
            print(f"Can't transfer, {error}.")

class interestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount*1.05)
        print("\nYour deposit is complete")
        self.getBalance()

class savingsAcc(interestRewardsAcc):
    def __init__(self, InitialDeposit, AccName):
        super().__init__(InitialDeposit, AccName)
        self.fee=5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Your withdraw was complete")
        except balanceFlag as error:
            print(f"Can't withdraw, {error}.")
        

