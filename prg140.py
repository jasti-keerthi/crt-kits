msg = input("Enter message: ").split()
print("OTP Extracted:", next(word for word in msg if word.isdigit() and len(word) == 6))