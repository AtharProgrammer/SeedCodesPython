'''
Assignment:
Create a class called BankAccount with attributes account_number, holder_name,
and balance. Implement methods to deposit money,
withdraw money (if sufficient balance is available),
and display the account details.
'''
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} successfully. Current balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance}")

# Test the BankAccount class
account1 = BankAccount("123456", "John Doe", 1000)
account1.display_details()
account1.deposit(500)
account1.withdraw(200)
account1.display_details()

account2 = BankAccount("987654", "Alice Smith", 200)
account2.display_details()
account2.withdraw(300)  # Insufficient balance
