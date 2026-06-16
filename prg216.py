'''11. Reverse and Add
Write a program to reverse a three-digit number and add it to the original number.'''
num = int(input("Enter a three-digit number: "))
first = num // 100
middle = (num // 10) % 10
last = num % 10
reverse =  last* 100 + middle*10 + first
result = num + reverse
print("Original number:",num)
print("reverse number:",reverse)
print("sum:",result)