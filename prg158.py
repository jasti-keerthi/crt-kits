''' Employee Work Hours
Problem Statement:
Create a class Employee with a method work_hours() that displays "Employee works 8 hours a day".
Create a class Intern that inherits from Employee and overrides the work_hours() method to display "Intern works 6 hours a day".
Test Case:
Input:
intern = Intern()
intern.work_hours()
Output:
Intern works 6 hours a day'''
class Employee:
    def work_hours(self):
        print("Employee works 8 hours a day")
class Intern(Employee): 
    def work_hours(self):
        print("Intern works 6 hours a day")
intern = Intern()
intern.work_hours()