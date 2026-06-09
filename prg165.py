'''Problem Statement
A company provides different bonus amounts based on employee roles.
Create a class Employee with a method bonus() that displays:
Bonus: ₹5000
Create a child class Manager that overrides the method and displays:
Bonus: ₹20000
Display the manager's bonus amount.
Test Case 1
Input
Manager
Output
Bonus: ₹20000
Test Case 2
Input
Employee
Output
Bonus: ₹5000'''
class Employee:
    def bonus(self):
        print("Bonus: ₹5000")
class Manager(Employee):
    def bonus(self):
        print("Bonus: ₹20000")
m1=Manager()
m1.bonus()
e1=Employee()
e1.bonus()