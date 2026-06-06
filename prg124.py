average=list(map(int,input('Enter the average : ').split()))
score=average=sum(average)/len(average)
print(f"Average NPS Score : {score:.2f}")