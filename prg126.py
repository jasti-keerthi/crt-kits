price=list(map(int,input('Enter the price : ').split()))
print(sorted(sorted(price,reverse=True))[:3])
