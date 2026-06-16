'''7. Average of Digits
Write a program to calculate the average of the digits in a three-digit number.
'''
num = int(input("Enter a three-digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
Average =(hundreds + tens + ones) / 3
print("Average of Digits:",Average)