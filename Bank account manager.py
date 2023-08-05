'''The goal is to create a bank account management class with the following features: account creation, money deposit, cash withdrawal, and balance view.
'''
class BankAccount():
    _account_number = 0
    @classmethod
    def _generate_account_number(cls):
        cls._account_number += 1
        return cls._account_number

    def __init__(self, holder):
        self.account_number = self._generate_account_number()
        self.holder = holder
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposit of {amount}€")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Withdrawal of {amount}€")
        else:
            print("Insufficient balance to make the withdrawal.")

    def display_history(self):
        print(f"Operations history for account {self.account_number}:")
        for operation in self.history:
            print(operation)

class Bank():
    def __init__(self):
        self.accounts = []

    def create_account(self, holder):
        new_account = BankAccount(holder)
        self.accounts.append(new_account)
        return new_account

    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def display_accounts(self):
        print("List of accounts in the bank:")
        for account in self.accounts:
            print(f"Account {account.account_number} - Holder: {account.holder}, Balance: {account.balance}€")

# Test the application
if __name__ == "__main__":
    bank = Bank()