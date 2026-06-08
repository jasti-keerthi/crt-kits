class Product:
    def __init__(self,name,price):
        print("Product object is created...!")
        self.name=name
        self.price=price
def details(self):
        print(self)
P1=Product('Phone',2000)
details(P1)
P2=Product('laptop',70000)
details(P2)
P3=Product('tv',50000)
details(P3)
P4=Product('car',200000)
details(P4)
P5=Product('cooler',5000)
details(P5)
print(f"name={P1.name}")
print(f"price={P1.price}")
print(f"name={P2.name}")
print(f"price={P2.price}")
print(f"name={P3.name}")
print(f"price={P3.price}")
print(f"name={P4.name}")
print(f"price={P4.price}")
print(f"name={P5.name}")
print(f"price={P5.price}")
