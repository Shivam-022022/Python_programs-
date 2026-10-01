class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self, years=1):
        return 0


class SavingsAccount(BankAccount):
    def calculate_interest(self, years=1):
        return self.balance * 4 * years / 100          # 4% simple interest


class CurrentAccount(BankAccount):
    def calculate_interest(self, years=1):
        return 0                                       # no interest on current accounts


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, years=1):
        return self.balance * ((1 + 0.07) ** years - 1)  # 7% compounded yearly


for acc in (SavingsAccount(100000), CurrentAccount(100000), FixedDepositAccount(100000)):
    print(f"{type(acc).__name__}: interest for 2 years = {round(acc.calculate_interest(2), 2)}")
