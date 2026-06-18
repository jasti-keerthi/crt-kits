# downward triangle of stars **** *** ** *
n = int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print("*", end=" ")
    print()