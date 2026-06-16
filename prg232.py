n = int(input("Enter the integer: "))

for i in range(1, n + 1):
    if i % 2 != 0:      # Odd row
        for j in range(1, n + 1):
            print(j, end=" ")
    else:               # Even row
        for j in range(n, 0, -1):
            print(j, end=" ")
    print()