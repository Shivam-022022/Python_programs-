from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    MIN_BALANCE = 1000

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs.{amount}. Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= self.MIN_BALANCE:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. Balance: Rs.{self.balance}")
        else:
            print("Withdrawal denied: minimum balance of Rs.1000 must be maintained.")


class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 20000

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs.{amount}. Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if self.balance + self.OVERDRAFT_LIMIT >= amount:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. Balance: Rs.{self.balance}")
        else:
            print("Withdrawal denied: overdraft limit exceeded.")


print("--- Savings Account ---")
sa = SavingsAccount("S101", 5000)
sa.deposit(2000)
sa.withdraw(3000)
sa.withdraw(4000)

print("--- Current Account ---")
ca = CurrentAccount("C201", 5000)
ca.deposit(1000)
ca.withdraw(15000)
ca.withdraw(15000)
