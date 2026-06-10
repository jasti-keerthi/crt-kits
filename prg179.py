class Member:
    def __init__(self, member_name):
        self.member_name = member_name
class MembershipPlan:
    def __init__(self, plan_name, monthly_fee):
        self.plan_name = plan_name
        self.monthly_fee = monthly_fee
class Gym:
    def __init__(self, duration):
        self.duration = duration
    def calculate_fee(self, plan):
        return self.duration * plan.monthly_fee
    def generate_receipt(self, member, plan):
        print("=" * 50)
        print("             MEMBERSHIP RECEIPT")
        print("=" * 50)
        print(f"Member Name : {member.member_name}")
        print(f"Plan        : {plan.plan_name}")
        print(f"Duration    : {self.duration} Months")
        print(f"Total Fee   : {self.calculate_fee(plan)}")
        print("=" * 50)
member = Member("Ava")
plan = MembershipPlan("Premium", 2000)
gym = Gym(6)
gym.generate_receipt(member, plan)