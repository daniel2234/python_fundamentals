class BankAccount:
    interest_rate = 0.11
    accounts = []

    @classmethod
    def create(cls):
        account = cls()
        cls.accounts.append(account)
        return account

    @classmethod
    def total_funds(cls):
        result = 0
        for account in cls.accounts:
            result += account.balance
        return result

    @classmethod
    def interest_time(cls):
        pass

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, number):
        self.balance += number

    def withdraw(self, number):
        self.balance -= number


my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance)
print(your_account.balance)
print(BankAccount.total_funds())
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance)  # 200
print(your_account.balance)  # 1000
print(BankAccount.total_funds())  # 1200
