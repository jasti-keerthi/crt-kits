balance = 5000
try:
    amount = int(input("Enter Withdrawl amount: "))

    if amount > balance:
        raise ValueError("Insufficient Balance")
    print("Withdrawl Successful")
except ValueError as e:
    print("Transaction Failed :", e)