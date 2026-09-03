# Create functions for deposit, withdrawal, balance enquiry, and transaction
# history. Prevent withdrawal when the balance is insufficient and maintain a
# transaction record.

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited: {amount}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            self.history.append(f"Failed withdrawal (insufficient funds): {amount}")
            return "Insufficient balance"
        self.balance -= amount
        self.history.append(f"Withdrew: {amount}")
        return self.balance

    def balance_enquiry(self):
        return self.balance

    def transaction_history(self):
        return self.history


if __name__ == "__main__":
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(5000)  # should fail

    print(f"Current Balance = {account.balance_enquiry()}")
    print("Transaction History:")
    for entry in account.transaction_history():
        print(f"  - {entry}")
