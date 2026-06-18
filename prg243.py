n=int(input('Enter the vibe  :'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
##########
n = int(input("Enter a value: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
####################
n = int(input("Enter a value: "))
for i in range(1, n + 1):
    if i % 2 == 1:
        print((str(i) + " ") * i)
    else:
        print(("* " ) * i)
###########################n = int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(j, end=" ")
        else:
            print("*", end=" ")
    print()