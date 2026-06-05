num=int(input("enter a number : "))
print(f"Multiplication table of {num}:")
for i in  range(10,0,-1):
    print(f"{num} x {i}= {num*i}")