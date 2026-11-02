class ATM:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Withdrew:", amount)

    def display_account_details(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

atm = ATM(name, balance)

while True:
    print("\n1.Check Balance 2.Deposit 3.Withdraw 4.Account Details 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)

    elif choice == 4:
        atm.display_account_details()

    elif choice == 5:
        break