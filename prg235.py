n = int(input("Enter the integer: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j % 2 == 0:
            print("Even", end=" ")
        else:
            print("Odd", end=" ")
    print()