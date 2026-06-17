'''# equalateral triangle of *
n=int(input("Enter a number:"))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)'''

'''# equalatral triangle of 1234
n=int(input("Enter a number:"))
k=1
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(k, end=" ")
        k += 1
    print()'''
'''#equalateral triangel of 1 22 333 444
n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print(i,end=" ")
        else:
            print(" ",end="")
    print()'''
'''#equalateral triangle of 1 2 3 4
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    k=1
    for j in range(n,0,-1):
        if j<=i:
            print(k,end=" ")
            k+=1
        else:
            print(" ", end="")
    print()'''
'''#equalateral triangle of 1 00 111 0000
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n,0,-1):
        if j<=i:
            if i%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        else:
            print(" ", end="")
    print()'''
'''#equalateral triangle of 1 10 101 1010
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n,0,-1):
        if(j<=i):
            if (i%2!=0):
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            print(" ", end="")
    print()'''
'''#equalateral triangle of 1 ** 111 ****
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n,0,-1):
        if(j<=i):
            if (i%2!=0):
                print("1",end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ", end="")
    print()'''
'''# equalateral triangle of * 11 *** 1111
n=int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n,0,-1):
        if(j<=i):
            if (i%2!=0):
                print("*",end=" ")
            else:
                print("1",end=" ")
        else:
            print(" ", end="")
    print()'''
'''#equalateral triangle of * *** ***** *******
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if n-i+1<=j<=n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''

'''# equalateral triangle of 1 222 33333 4444444
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if n-i+1<=j<=n+i-1:
            print(i, end="")
        else:
            print(" ", end="")
    print()'''
#equalateral triangle of 1 121 12321 1234321
n = int(input("Enter number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()