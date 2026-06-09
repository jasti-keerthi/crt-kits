'''Problem Statement
A video streaming platform offers different viewing experiences based on the subscription plan.
Create a class Subscription with a method features() that displays:
Watch videos with advertisements
Create a child class PremiumSubscription that overrides the method and displays:
Watch videos without advertisements
Display the premium subscription features.
Test Case 1
Input
Premium Plan
Output
Watch videos without advertisements
Test Case 2
Input
Basic Plan
Output
Watch videos with advertisements'''
class Subscription:
    def features(self):
        print("Watch videos with advertisements")
class PremiumSubscription(Subscription):
    def features(self):
        print("Watch videos without advertisements")
p1=PremiumSubscription()
p1.features()
s1=Subscription()
s1.features()