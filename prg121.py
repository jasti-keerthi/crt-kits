marks=list(map(int,input('Enter the marks : ').split()))
print(f"ranked :{sorted(marks,reverse=True)} | top marks : {max(marks)}")
