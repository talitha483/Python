# class BankAccount:
class BankAccount:

    # def ...(self, ...):
    def __init__(self, name):
        self.name = name
        self.balance = 0

    # def deposit(self, ...):
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"   # return ...

    # def withdraw(self, ...):
    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

# Test
account = BankAccount("Name")
print(account.deposit(1000))  # Expected: Deposited 1000. New balance: 1000
print(account.withdraw(500))  # Expected: Withdrew 500. New balance: 500
print(account.withdraw(600))  # Expected: Invalid withdrawal amount or insufficient funds
