'''Problem Statement
A food delivery company offers different delivery charges based on the customer type.
-->Create a class Customer with a method delivery_charge() that displays a standard delivery charge of ₹50.
-->Create a child class PrimeCustomer that overrides the delivery_charge() method and displays a discounted delivery charge of ₹20.
Write a program to create an object of PrimeCustomer and display the delivery charge.
Test Case 1:
Input:
Prime Customer
Output:
Delivery Charge: ₹20'''
class RegularCustomer:
    def delivery_charge(self):
        print("Delivery Charge: 50")
class PrimeCustomer(RegularCustomer):
    def delivery_charge(self):
        print("Delivery Charge: 20")
customer = PrimeCustomer()
customer.delivery_charge()
customer = RegularCustomer()
customer.delivery_charge()