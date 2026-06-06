price=list(map(int,input('Enter the prices: ').split()))
print([i for i in price if i>1000])