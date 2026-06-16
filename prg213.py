'''
8. Largest Digit
Write a program to find the largest digit in a three-digit number.
'''
num = int(input("Enter a three-digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
largest = max( hundreds , tens , ones)
print("Largest Digit:",largest )
