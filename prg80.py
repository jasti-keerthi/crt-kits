grand_total = 0

num_pizzas = int(input("Enter the number of pizzas you want to order: "))

for p in range(num_pizzas):
    size = input("Enter the size of pizza (small/medium/large): ").lower()
    if size == "small":
        total_bill = 10
    elif size == "medium":
        total_bill = 15
    elif size == "large":
        total_bill = 20
    else:
        print("Invalid size! Skipping this pizza.")
    num_toppings = int(input("Enter the number of toppings: "))

    for i in range(num_toppings):
        topping = input("Enter your topping: ").lower()
        if topping == "cheese":
            total_bill += 2
        elif topping == "pepperoni":
            total_bill += 3
        elif topping == "olives":
            total_bill += 5
        elif topping == "jalapenos":
            total_bill += 5
        else:
            print("Invalid topping!")
    grand_total += total_bill
if grand_total < 50:
    delivery_charge = 5
else:
    delivery_charge = 0
final_amount = grand_total + delivery_charge
print("Order Value: $", grand_total)
print("Delivery Charge: $", delivery_charge)
print("Final Amount: $", final_amount)