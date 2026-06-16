'''
2. Sum of Digits
Write a program to find the sum of all digits in a three-digit number.
'''
num = int(input("Enter a three-digit number: "))
sum_digits = 0
while num != 0:
    rem = num % 10
    sum_digits += rem
    num = num // 10
print("Sum of digits is", sum_digits)