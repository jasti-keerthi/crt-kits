'''
4. Swap First and Last Digit
Write a program to swap the first and last digits of a three-digit number.
'''
num = int(input("Enter a three-digit number: "))
first = num // 100
middle = (num // 10) % 10
last = num % 10
swapped = last * 100 + middle * 10 + first
print("Number after swapping first and last digits:", swapped)