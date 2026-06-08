class employee():
    def __init__(self,empname,empid,job,salary):
        self.empname=empname
        self.empid=empid
        self.job=job
        self.salary=salary
def details(self):
        print(self)
        print(f"empname is {self.empname}")
        print(f"empid is {self.empid}")
        print(f"job is {self.job}")
        print(f"salary is {self.salary}")
        print("----------------")
e1=employee('scott',4336,'develeper',50000)
details(e1)
