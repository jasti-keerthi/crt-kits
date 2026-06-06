booked=list(map(int,input("Enter the booked slots  :").split()))
requested=list(map(int,input("Enter the requesteed slots :").split()))
print("slot already booked" if requested in booked else "slot is available")
