'''9. Smallest Digit
Write a program to find the smallest digit in a three-digit number.
'''
num = int(input("Enter a three-digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
smallest = min( hundreds , tens , ones)
print("smallest Digit:",smallest )
