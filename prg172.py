class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number
class ParkingSlot:
    def __init__(self, slot_number):
        self.slot_number = slot_number
class ParkingManager:
    def __init__(self, vehicle, hours_parked, rate_per_hour):
        self.vehicle = vehicle
        self.hours_parked = hours_parked
        self.rate_per_hour = rate_per_hour
    def calculate_fee(self):
        return self.hours_parked * self.rate_per_hour
    def generate_receipt(self):
        fee = self.calculate_fee()
        print("=" * 50)
        print("PARKING RECEIPT")
        print("=" * 50)
        print(f"Vehicle Number : AP39AB1234")
        print(f"Hours Parked   : {self.hours_parked}")
        print(f"Parking Fee    : Rs.{fee}")
        print("=" * 50)
vehicle_number = input("Vehicle Number : AP39AB1234")
hours = int(input("Hours Parked   : "))
rate = int(input("Rate Per Hour  : "))
vehicle = Vehicle(vehicle_number)
manager = ParkingManager(vehicle, hours, rate)
manager.generate_receipt()