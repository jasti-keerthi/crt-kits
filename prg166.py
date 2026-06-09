'''Problem Statement
A training institute determines placement eligibility differently for regular students and advanced-track students.
Create a class Student with a method placement_status() that displays:
Placement Eligibility: Assessment Score Above 60
Create a child class AdvancedStudent that overrides the method and displays:
Placement Eligibility: Assessment Score Above 80
Display the eligibility criteria for an advanced-track student.
Test Case 1
Input
Advanced Student
Output
Placement Eligibility: Assessment Score Above 80
Test Case 2
Input
Regular Student
Output
Placement Eligibility: Assessment Score Above 60
'''
class Student:
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 60")
class AdvancedStudent(Student):
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 80")
a1=AdvancedStudent()
a1.placement_status()
s1=Student()
s1.placement_status()