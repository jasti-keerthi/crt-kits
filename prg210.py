'''
5. Sum of First and Last Digit
Write a program to find the sum of the first and last digit of a three-digit number.
'''
num = int(input("Enter a three-digit number: "))
first = num // 100
last = num % 10
sum_digit = first + last
print("sum of first and last digit:",sum_digit)