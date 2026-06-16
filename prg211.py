'''6. Extract Individual Digits
Write a program to extract and display each digit of a three-digit number separately.'''
num = int(input("Enter a three-digit number: "))
hundereds = num // 100
tens = (num // 10) % 10
ones = num % 10
print("Hundereds",hundereds)
print("tens",tens)
print("ones",ones)