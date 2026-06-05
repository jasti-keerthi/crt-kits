num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(f"Multiplication table of {i}")
    print("-"*23)
    for j in range(10,0,-1):
        print(f"{i}x{j}={i*j}")