class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
class Movie:
    def __init__(self, movie_name, ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
class Booking:
    def __init__(self, customer, movie, number_of_tickets):
        self.customer = customer
        self.movie = movie
        self.number_of_tickets = number_of_tickets
    def calculate_amount(self):
        return self.movie.ticket_price * self.number_of_tickets
    def book_ticket(self):
        return "CONFIRMED"
    def generate_receipt(self):
        total_amount = self.calculate_amount()
        print("=" * 50)
        print("            MOVIE BOOKING RECEIPT")
        print("=" * 50)
        print()
        print(f"Customer Name   : {self.customer.customer_name}")
        print(f"Movie Name      : {self.movie.movie_name}")
        print()
        print(f"Ticket Price    : ₹{self.movie.ticket_price}")
        print(f"Tickets Booked  : {self.number_of_tickets}")
        print()
        print("-" * 50)
        print()
        print(f"Total Amount    : ₹{total_amount}")
        print()
        print(f"Booking Status  : {self.book_ticket()}")
        print()
        print("=" * 50)
customer_name = input("Enter the  customer name:")
movie_name = input("Enter the novie name:")
ticket_price = int(input("price of tickets:"))
number_of_tickets = int(input("Enter no.of tickets"))
customer = Customer(customer_name)
movie = Movie(movie_name, ticket_price)
booking = Booking(customer, movie, number_of_tickets)
booking.generate_receipt()