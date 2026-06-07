ifsc = input("Enter IFSC Code: ")

if len(ifsc) != 11:
    print("Invalid — IFSC code must be 11 characters long")

elif not ifsc[:4].isalpha():
    print("Invalid — First 4 characters must be alphabets")

elif ifsc[4] != '0':
    print("Invalid — 5th character must be '0'")

elif not ifsc[5:].isalnum():
    print("Invalid — Last 6 characters must be alphanumeric")

else:
    print("Valid IFSC Code")