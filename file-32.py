# Develop a package banking containing:
#   a) account.py      -- account creation and balance
#   b) transaction.py  -- deposit and withdrawal
#   c) loan.py         -- loan calculation
# Create a main program to use the package.
#
# NOTE: A real package would be a "banking/" directory with __init__.py,
# account.py, transaction.py, and loan.py as separate files. It is
# simulated here in one file using clearly labelled sections so it
# matches the file-XX.py naming convention.

# ---------- banking/account.py ----------
def create_account(name, initial_balance=0):
    return {"name": name, "balance": initial_balance}
# ---------- end banking/account.py ----------


# ---------- banking/transaction.py ----------
def deposit(account, amount):
    account["balance"] += amount
    return account["balance"]


def withdraw(account, amount):
    if amount > account["balance"]:
        return "Insufficient balance"
    account["balance"] -= amount
    return account["balance"]
# ---------- end banking/transaction.py ----------


# ---------- banking/loan.py ----------
def calculate_loan_emi(principal, annual_rate, years):
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12
    if monthly_rate == 0:
        return principal / months
    emi = principal * monthly_rate * (1 + monthly_rate) ** months / \
        ((1 + monthly_rate) ** months - 1)
    return emi
# ---------- end banking/loan.py ----------


if __name__ == "__main__":
    account = create_account("Ritesh Agale", 5000)
    deposit(account, 2000)
    withdraw(account, 1000)

    print(f"Account: {account}")
    print(f"Monthly EMI for loan of 500000 @ 8.5% for 5 years: "
          f"{calculate_loan_emi(500000, 8.5, 5):.2f}")
