revenue=list(map(int,input("enter the revenue for 7 days :").split()))
print(f"Total Revenue :{sum(revenue)} | best Day :{max(revenue)} | worst day :{min(revenue)}")