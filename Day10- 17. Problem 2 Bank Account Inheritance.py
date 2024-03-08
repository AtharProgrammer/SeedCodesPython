'''
Problem 2: Bank Account Inheritance
Create a class Account with attributes account_number, holder_name,
and balance. Implement a method display_info() to print all the account
information. Then, define two subclasses SavingsAccount and CheckingAccount,
each with an additional attribute and a method to deduct a fee from the account.

'''
class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: ${self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def deduct_fee(self, fee):
        self.balance -= fee

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.interest_rate}%")

class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def deduct_fee(self, fee):
        self.balance -= fee

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: ${self.overdraft_limit}")

# Test
savings_account = SavingsAccount("SA123", "Alice", 5000, 0.5)
savings_account.deduct_fee(20)
savings_account.display_info()

checking_account = CheckingAccount("CA456", "Bob", 3000, 100)
checking_account.deduct_fee(10)
checking_account.display_info()
