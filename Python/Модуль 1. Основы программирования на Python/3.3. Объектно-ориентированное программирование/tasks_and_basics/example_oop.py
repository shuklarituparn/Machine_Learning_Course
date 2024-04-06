# Encapsulation: the BankAccount class hides the internal details of the account balance
class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance

# Polymorphism: the BankAccount and SavingsAccount classes both implement the Account interface
class Account:
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

class BankAccount(Account):
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

class SavingsAccount(Account):
    def __init__(self, interest_rate):
        self._balance = 0
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def calculate_interest(self):
        return self._balance * self.interest_rate

    def get_balance(self):
        pass


# Abstraction: the AccountManager class hides the details of how accounts are managed
class AccountManager:
    def __init__(self):
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def remove_account(self, account):
        self._accounts.remove(account)

    def process_transactions(self):
        for account in self._accounts:
            account.deposit(10)
            account.withdraw(5)

class Person:
    def __init__(self, name, surname):
        self.name=name
        surname=surname  #No error a

    def greet(self):
        print(f"Hello, {self.name}")


if __name__ == "__main__":
    Person('Anna', 'Moroz').greet()
    bank_account = BankAccount()
    savings_account = SavingsAccount(0.05)
    bank_account.deposit(100)
    bank_account.withdraw(50)
    savings_account.deposit(200)
    savings_account.withdraw(100)
    account_manager = AccountManager()
    account_manager.add_account(bank_account)
    account_manager.add_account(savings_account)
    account_manager.process_transactions()
    print(savings_account.calculate_interest())  # Output: 5.25