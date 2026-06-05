# Input list
numbers = int(input("enter list :"))  # You can change this to any list

# Separate even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Display results
print("Even numbers:", even_numbers)
print("Count of even numbers:", len(even_numbers))
print("Odd numbers:", odd_numbers)
print("Count of odd numbers:", len(odd_numbers))
