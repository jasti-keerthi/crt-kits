'''
Problem Statement
A ride-booking application offers different fare structures for normal and luxury rides.
Create a class Ride with a method fare() that displays:
Fare: ₹100
Create a child class LuxuryRide that overrides the method and displays:
Fare: ₹300
Display the fare of a luxury ride.
Test Case 1
Input:
Luxury Ride
Output:
Fare: ₹300
Test Case 2
Input:
Normal Ride
Output:
Fare: ₹100
'''
class Ride:
    def fare(self):
        print("Fare: 100/-")
class LuxuryRide( Ride ):
    def fare(self):
        print("Fare: 300/-")
r1=LuxuryRide()
r1.fare()
r2=Ride()
r2.fare()