class Customer:
    def __init__(self, customer_name, mobile_number):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
class RechargePlan:
    def __init__(self, plan_name, amount):
        self.plan_name = plan_name
        self.amount = amount
class Recharge:
    def select_plan(self, plan):
        self.plan = plan
    def generate_receipt(self, customer):
        print("=" * 50)
        print("RECHARGE RECEIPT")
        print("=" * 50)
        print(f"Customer Name : {customer.customer_name}")
        print(f"Plan Selected : {self.plan.plan_name}")
        print(f"Amount Paid   : {self.plan.amount}")
        print("Status : SUCCESSFUL")
        print("=" * 50)
customer = Customer("James", "9876543210")
plan = RechargePlan("Unlimited 84 Days", 799)
recharge = Recharge()
recharge.select_plan(plan)
recharge.generate_receipt(customer)