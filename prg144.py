class mobile():
    def __init__(self,brand,price,color):
        print(" Mobile market...!")
        self.brand=brand
        self.price=price
        self.color=color
def details(self):
        print(self)
        print(f"brand is {self.brand}")
        print(f"price is {self.price}")
        print(f"color is {self.color}")
        print("----------------------")
m1=mobile('redmi',25000,'red')
details(m1)
m2=mobile('realme',10000,'black')
details(m2)
m3=mobile('oppo',16000,'blue')
details(m3)
m4=mobile('iphone',100000,'pink')
details(m4)
m5=mobile('sumsung',60000,'sliver')
details(m5)
