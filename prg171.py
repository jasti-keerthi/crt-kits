class Passenger:
    def __init__(self, pass_name):
        self.pass_name = pass_name
class Flight:
    def __init__(self, flight_num):
        self.flight_num = flight_num
    def assign_seat(self, seat_num):
        self.seat_num = seat_num
        return True
class BoardingPass:
    def __init__(self, passenger, flight, seat_num):
        self.passenger = passenger
        self.flight = flight
        self.seat_num = seat_num
    def generate_boarding_pass(self):
        print("=" * 50)
        print("BOARDING PASS")
        print("=" * 50)
        print(f"Passenger Name : {self.passenger.pass_name}")
        print(f"Flight Number  : {self.flight.flight_num}")
        print(f"Seat Number    : {self.seat_num}")
        print("Status: CHECK-IN COMPLETE")
        print("=" * 50)
class Airport:
    def __init__(self):
        self.passengers = []
    def register_passenger(self, passenger):
        self.passengers.append(passenger)
airport = Airport()
name = input("Passenger : ")
flight_num = input("Flight : ")
seat_num = input("Seat : ")
passenger = Passenger(name)
flight = Flight(flight_num)
airport.register_passenger(passenger)
if flight.assign_seat(seat_num):
    boarding_pass = BoardingPass(passenger, flight, seat_num)
    boarding_pass.generate_boarding_pass()
else:
    print("Seat already occupied!")