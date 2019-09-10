class User:		# declare a class and give it name User
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_info_account()

    def make_transfer_money(self, other_user, amount):
        self.account.transfer_money(other_user, amount)
        return self

class BankAccount:
    def __init__(self):
        self.int_rate = int_rate
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        
    
    def withdraw(self, amount):
        self.balance -= amount

    def display_info_account(self):
        print('BALANCE: ', self.balance)

    def yield_interest(self):
        self.balance += self.balance * self.int_rate

    def transfer_money(self, other_account, amount):
        self.balance -= amount
        other_account.balance += amount

account1 = BankAccount(4)
account1.deposit(400)
print(account1.balance)

cean = User("cean", "cean@gmail.com", BankAccount(4))
cean.account.display_info_account()

# cean.make_deposit(500).make_withdrawal(100)
# print(cean.account.balance)
# test1 = User("test1", "test1@gmail.com")
# test.make_deposit(40).make_deposit(40).make_withdrawal(20).make_withdrawal(20).display_user_balance()

# test1.make_deposit(400).make_withdrawal(30).make_withdrawal(30).make_withdrawal(30).display_user_balance()

# cean.transfer_money(test1, 30)