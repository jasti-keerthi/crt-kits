pin=int(input("Enter your pin : "))
acc_bal=0
if pin==1234:
    print("welcome to the bank")
#DEposite,withdrawal,balance inquiry and exit.
    while True:
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Balance Inquiry")
        print("4. Exit")

        choice=int(input("Enter your choice : "))
        print("\n")
        if(choice==1):
            amount=int(input("Enter the amount to deposite : "))
            acc_bal=acc_bal+amount
            print(f"Dear customer your account xxxxxxxxxx1234 is crediteed with {amount}")
        elif(choice==2):
            amount=int(input("Enter the amount to withdraw : "))
            if(amount<acc_bal):
                print(f"Dear customer your account xxxxxxxxxx1234 is debited with {amount}")
                acc_bal=acc_bal+amount
            else:
                print("Insufficent balance")
        elif(choice==3):
            print(f"Dear customer your account xxxxxxxxxx1234 has {acc_bal} .")
        else:
            print("Thank you .......!")
            break
else:
    print("you Enterd Wrong pin .")