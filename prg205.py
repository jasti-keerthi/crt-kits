'''1. Reverse a Three-Digit Number
Write a program to reverse a three-digit number without converting it into a string.
'''
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)