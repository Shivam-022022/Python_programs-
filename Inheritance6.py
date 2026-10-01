class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Number :", self.account_number)
        print("Balance        :", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self, years=1):
        return self.balance * self.interest_rate * years / 100

    def display(self):
        super().display()
        print("Interest Rate  :", self.interest_rate, "%")


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, benefits):
        super().__init__(account_number, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        super().display()
        print("Benefits       :", ", ".join(self.benefits))


acc = PremiumSavingsAccount(
    "SB1001", 200000, 6,
    ["Free Debit Card", "Priority Banking", "Zero Charges on Transfers"]
)
acc.display()
print("Interest for 2 years:", acc.calculate_interest(2))
