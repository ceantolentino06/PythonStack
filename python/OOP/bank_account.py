class BankAccount:
    def __init__(self, int_rate):
        self.int_rate = int_rate / 100
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_info_account(self):
        print('BALANCE: ', self.balance)

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

account1 = BankAccount(4)
account2 = BankAccount(6)

account1.deposit(300).deposit(200).deposit(350).withdraw(200).yield_interest().display_info_account()
account2.deposit(400).deposit(400).withdraw(100).withdraw(220).yield_interest().display_info_account()
    