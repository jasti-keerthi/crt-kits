class Student:
    def __init__(self, student_id, student_name, attendance):
        self.student_id = student_id
        self.student_name = student_name
        self.attendance = attendance
class Assessment:
    def __init__(self, assessment_score):
        self.assessment_score = assessment_score
class PlacementManager:
    def __init__(self):
        self.students = []
    def add_student(self, student, assessment):
        self.students.append((student, assessment))
    def check_eligibility(self, attendance, score):
        return attendance >= 75 and score >= 60
    def generate_report(self):
        for student, assessment in self.students:
            status = "ELIGIBLE" if self.check_eligibility(student.attendance, assessment.assessment_score) else "NOT ELIGIBLE"
            print("=" * 50)
            print("PLACEMENT ELIGIBILITY REPORT")
            print("=" * 50)
            print(f"Student ID       : {student.student_id}")
            print(f"Student Name     : {student.student_name}")
            print(f"Attendance       : {student.attendance}%")
            print(f"Assessment Score : {assessment.assessment_score}")
            print(f"Placement Status : {status}")
            print("=" * 50)
student_id = input("Student ID: ")
student_name = input("Student Name: ")
attendance = int(input("Attendance: "))
assessment_score = int(input("Assessment Score: "))
student = Student(student_id, student_name, attendance)
assessment = Assessment(assessment_score)
manager = PlacementManager()
manager.add_student(student, assessment)
manager.generate_report()