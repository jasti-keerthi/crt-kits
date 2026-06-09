class vehicle:
    def __init__(self, b, p, c, s):
        self.b = b
        self.p = p
        self.c = c
        self.s = s
        print("Vehicle class Constructor")


class bike(vehicle):
    def __init__(self, b, p, c, s, g, m):
        super().__init__(b, p, c, s)
        self.g = g
        self.m = m
        print("Bike class Constructor")     #mulitlevel inheritance


class sportsbike(bike):
    def __init__(self, b, p, c, s, g, m, speed):
        super().__init__(b, p, c, s, g, m)
        self.speed = speed
        print("Sportsbike class Constructor")

b1 = sportsbike("Tata", 25000, "Black", 2, 3, 45, 180)