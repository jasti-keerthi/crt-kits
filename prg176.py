class Client:
    def __init__(self, client_name):
        self.client_name = client_name
class Project:
    def __init__(self, project_name, hourly_rate):
        self.project_name = project_name
        self.hourly_rate = hourly_rate
class Invoice:
    def __init__(self, hours_worked):
        self.hours_worked = hours_worked
    def calculate_amount(self, project):
        return self.hours_worked * project.hourly_rate
    def generate_invoice(self, client, project):
        print("=" * 50)
        print(" CLIENT INVOICE")
        print("=" * 50)
        print(f"Client Name   : {client.client_name}")
        print(f"Project Name  : {project.project_name}")
        print(f"Hours Worked  : {self.hours_worked}")
        print(f"Total Amount  : ₹{self.calculate_amount(project)}")
        print("=" * 50)
client = Client("Arjun")
project = Project("Portfolio Website", 1000)
invoice = Invoice(20)
invoice.generate_invoice(client, project)