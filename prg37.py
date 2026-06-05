num=int(input("enter a number : "))
for i in range(1,num+1):
    print(f"Multiplication table of {num}:")
    print("------------------------------")
    for j in range(1,11):
         print(f"{i} x {j} = {i*j}")