class student():
    def __init__(self,name,age):
        print("Student object is creted...!")
        self.name=name
        self.age=age
def details(self):
    print("------------")
    print(f"name is {self.name}")
    print(f"name is {self.age}")
s1=student('keerthi',21)
details(s1)
s2=student('harsha',21)
details(s2)
s3=student('prameela',21)
details(s3)
