class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self.balance
    
    def withdraw(self, withdrawal_amount):
        self.balance -= withdrawal_amount
        return self.balance
    
account = BankAccount("Darcy")
print(account.deposit(10.5))
print(account.withdraw(4.25))
        