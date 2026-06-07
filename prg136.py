first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
phone = input("Enter Phone Number: ")

first2_first = first_name[:2].upper()
first2_last = last_name[:2].upper()
last2_phone = phone[-2:]

pnr = first2_first + first2_last + last2_phone

print("PNR:", pnr)