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
        print("Bike class Constructor")


class car(vehicle):
    def __init__(self, b, p, c, s, fuel):           #hierarchical inheritance
        super().__init__(b, p, c, s)
        self.fuel = fuel
        print("Car class Constructor")


# Object of bike
b1 = bike("Honda", 25000, "Black", 2, 5, 45)

print()

# Object of car
c1 = car("Tata", 800000, "White", 4, "Petrol")