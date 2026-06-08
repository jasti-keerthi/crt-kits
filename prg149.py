class vehicle:
    def __init__(self,b,p,c,s):
        self.b=b
        self.p=p
        self.c=c
        self.s=s
        print('Vehicle class Constructor')
class bike(vehicle):
    def __init__(self, b, p, c, s,g,m):
        super().__init__(b, p, c, s)
        self.g=g
        self.m=m
        print('bike class constructor')
b1=bike('Tata',25000,'black',2,3,45)
