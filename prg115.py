n=7
revenue=[]
for i in range(n):
    ele = int(input(f"Enter the revenue for day {i+1} : "))
    revenue.append(ele)
print(f"Total Revenue :{sum(revenue)} | best Day :{max(revenue)} | worst day :{min(revenue)}")