class Guest:
    def __init__(self, guest_name):
        self.guest_name = guest_name
class Room:
    def __init__(self, room_type, room_rate):
        self.room_type = room_type
        self.room_rate = room_rate
class Reservation:
    def __init__(self, nights):
        self.nights = nights
    def calculate_amount(self, room):
        return room.room_rate * self.nights
    def generate_invoice(self, guest, room):
        print("=" * 50)
        print("HOTEL INVOICE")
        print("=" * 50)
        print(f"Guest Name     : {guest.guest_name}")
        print(f"Room Type      : {room.room_type}")
        print(f"Nights Stayed  : {self.nights}")
        print(f"Total Amount   : ₹{self.calculate_amount(room)}")
        print("=" * 50)
guest = Guest("Sophia")
room = Room("Deluxe", 3500)
reservation = Reservation(3)
reservation.generate_invoice(guest, room)