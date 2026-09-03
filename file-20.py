# Store deposits and withdrawals in a file. Read the file and calculate:
# - Total deposits
# - Total withdrawals
# - Final balance
# - Largest transaction

def create_transactions_file(filename):
    transactions = ["DEPOSIT,5000", "WITHDRAW,2000", "DEPOSIT,3000", "WITHDRAW,1000", "DEPOSIT,7000"]
    with open(filename, "w") as f:
        f.write("\n".join(transactions) + "\n")


def read_transactions(filename):
    transactions = []
    with open(filename, "r") as f:
        for line in f:
            t_type, amount = line.strip().split(",")
            transactions.append((t_type, int(amount)))
    return transactions


def total_deposits(transactions):
    return sum(amt for t, amt in transactions if t == "DEPOSIT")


def total_withdrawals(transactions):
    return sum(amt for t, amt in transactions if t == "WITHDRAW")


def final_balance(transactions):
    return total_deposits(transactions) - total_withdrawals(transactions)


def largest_transaction(transactions):
    return max(transactions, key=lambda t: t[1])


if __name__ == "__main__":
    create_transactions_file("transactions.csv")
    transactions = read_transactions("transactions.csv")

    print(f"Total Deposits: {total_deposits(transactions)}")
    print(f"Total Withdrawals: {total_withdrawals(transactions)}")
    print(f"Final Balance: {final_balance(transactions)}")
    print(f"Largest Transaction: {largest_transaction(transactions)}")
