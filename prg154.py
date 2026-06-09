class vehicle:
    def __init__(self, b, p, c, s):
        self.b = b
        self.p = p
        self.c = c
        self.s = s
        print("Vehicle class Constructor")


class engine:
    def __init__(self, mileage):
        self.mileage = mileage
        print("Engine class Constructor")


class bike(vehicle, engine):      # Hybrid Inheritance
    def __init__(self, b, p, c, s, g, m):
        vehicle.__init__(self, b, p, c, s)
        engine.__init__(self, m)

        self.g = g
        print("Bike class Constructor")


b1 = bike("Tata", 25000, "Black", 2, 3, 45)
