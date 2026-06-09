class vehicle:
    def __init__(self, b, p, c, s):
        self.b = b
        self.p = p
        self.c = c
        self.s = s
        print("Vehicle class Constructor")


class engine:
    def __init__(self, cc):
        self.cc = cc
        print("Engine class Constructor")          #multiple inheritance


class bike(vehicle, engine):
    def __init__(self, b, p, c, s, cc, g, m):
        vehicle.__init__(self, b, p, c, s)
        engine.__init__(self, cc)
        self.g = g
        self.m = m
        print("Bike class Constructor")


b1 = bike("Tata", 25000, "Black", 2, 150, 3, 45)