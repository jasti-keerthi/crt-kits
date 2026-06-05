str = input("Enter your full name: ")
print(str.casefold())
print(str.replace(" ", ""))
email = str.replace(" ", "").casefold() + "@company.com"
print("Your email is:", email)