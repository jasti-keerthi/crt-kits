class Owner:
    def __init__(self, owner_name):
        self.owner_name = owner_name
class Pet:
    def __init__(self, pet_name):
        self.pet_name = pet_name
class Appointment:
    def __init__(self, service, charge):
        self.service = service
        self.charge = charge
    def generate_receipt(self, owner, pet):
        print("=" * 50)
        print("            SERVICE RECEIPT")
        print("=" * 50)
        print(f"Owner Name : {owner.owner_name}")
        print(f"Pet Name   : {pet.pet_name}")
        print(f"Service    : {self.service}")
        print(f"Amount     : {self.charge}")
        print("=" * 50)
owner = Owner("parimala")
pet = Pet("Bruno")
appointment = Appointment("Grooming", 800)
appointment.generate_receipt(owner, pet)