class customer():
    def __init__(self):
        pass
    def set_name(self,name):
        self.name=name
    def set_id(self,id):
        self.id=id
    def set_age(self,age):
        self.age=age
    def get_name(self):
        print(f"name is {self.name}")
    def get_id(Self):
        print(f"id is {Self.id}")
    def get_age(self):
        print(f"age is {self.age}")
c1=customer()
c1.set_name('scott')
c1.set_id(123)
c1.set_age(21)
c1.get_name()
c1.get_id()
c1.get_age()