'''10. Check Palindrome Number
Write a program to check whether a three-digit number remains the same after reversing.'''
num = int(input("Enter a three-digit number: "))
first = num // 100
middle = (num // 10) % 10
last = num % 10
reverse =  last* 100 + middle*10 + first
if num == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")
