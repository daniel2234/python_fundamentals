class BankAccount:
    def __init__(self, balance, interest_rate=0):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return "Current Balance:{} with interest rate of {}".format(self.balance, self.interest_rate)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def gain_interest(self, interest):
        return self.balance * (1 + interest)


bankAccount = BankAccount(1000)
print('account balance', bankAccount)
bankAccount.deposit(100)
print(bankAccount)
bankAccount.withdraw(200)
print(bankAccount)
print(bankAccount.gain_interest(0.15))
