'''
3. Product of Digits
Write a program to find the product of all digits in a three-digit number.
'''
num = int(input("Enter a three-digit number: "))
product_digits = 1
while num != 0:
    rem = num % 10
    product_digits *= rem
    num = num // 10
print("Sum of digits is", product_digits)