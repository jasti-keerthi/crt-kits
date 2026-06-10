class User:
    def __init__(self, user_name):
        self.user_name = user_name
class Wallet:
    def __init__(self, balance):
        self.balance = balance
class Transaction:
    def __init__(self, transfer_amount):
        self.transfer_amount = transfer_amount
    def generate_receipt(self, user, wallet):
        current_balance = wallet.balance - self.transfer_amount
        print("=" * 50)
        print("TRANSACTION RECEIPT")
        print("=" * 50)
        print(f"User Name       : {user.user_name}")
        print(f"Opening Balance : {wallet.balance}")
        print(f"Transfer Amount : {self.transfer_amount}")
        print(f"Current Balance : {current_balance}")
        print("Status : SUCCESSFUL")
        print("=" * 50)
user = User("Gowri")
wallet = Wallet(10000)
transaction = Transaction(2500)
transaction.generate_receipt(user, wallet)