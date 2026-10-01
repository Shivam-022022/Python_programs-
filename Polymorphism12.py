class Payment:
    def make_payment(self, amount):
        print("Processing payment of Rs.", amount)


class UPIPayment(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def make_payment(self, amount):
        print(f"Paid Rs.{amount} using UPI ID {self.upi_id}")


class CardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def make_payment(self, amount):
        print(f"Paid Rs.{amount} using card ending {self.card_number[-4:]}")


class WalletPayment(Payment):
    def __init__(self, wallet_name, balance):
        self.wallet_name = wallet_name
        self.balance = balance

    def make_payment(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Paid Rs.{amount} from {self.wallet_name} wallet. Balance: Rs.{self.balance}")
        else:
            print(f"Insufficient balance in {self.wallet_name} wallet.")


def checkout(payment_method, amount):
    payment_method.make_payment(amount)


checkout(UPIPayment("amit@upi"), 1500)
checkout(CardPayment("1234567812345678"), 2500)
checkout(WalletPayment("PayWallet", 1000), 800)
