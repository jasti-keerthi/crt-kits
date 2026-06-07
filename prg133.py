template = input("Enter template: ")

name = input("Enter name: ")
product = input("Enter product: ")
discount = int(input("Enter discount: "))

user_data = {
    "name": name,
    "product": product,
    "discount": discount
}

message = template.format(**user_data)

print("Personalized Message:")
print(message)
