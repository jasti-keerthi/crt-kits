size = input("Enter the size of pizza: ").lower()

if size == "small":
    total_bill = 10
elif size == "medium":
    total_bill = 15
elif size == "large":
    total_bill = 20
else:
    print("Enter the valid sise - small/medium/large")
    
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
        print("Enter a valid topping - cheese,pepperoni,olives,jalapenos")
        

print("Total bill: $" + str(total_bill))