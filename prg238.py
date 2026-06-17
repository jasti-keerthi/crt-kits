n=int(input("Enter the integer :"))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(chr(i+64),end= "  ")
    print()


n=int(input("Enter the integer :"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(chr(j+64),end= "  ")
    print()

n=int(input("Enter the integer :"))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(chr(i+96),end= "  ")
    print()

n=int(input("Enter the integer :"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(chr(j+96),end= "  ")
    print()


n=int(input("Enter the number :"))
k=1
for i in range(n):
    for j in range(n):
        print(chr(k+64),end= "  ")
        if(k<26):
            k+=1
        else:
            k=1
    print()

n=int(input("Enter the number :"))
k=1
for i in range(n):
    for j in range(n):
        print(chr(k+96),end= "  ")
        if(k<26):
            k+=1
        else:
            k=1
    print()

n = int(input("Enter the value : "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(j+64), end=" ")
    print()

n = int(input("Enter the value : "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(j+96), end=" ")
    print()

n = int(input("Enter the value : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(69+i-j), end=" ")
    print()

n = int(input("Enter number of letter rows: "))
letter = 65  
for i in range(n * 2 - 1):
    if i % 2 == 0:
        ch = chr(letter)
        for j in range(n):
            print(ch, end=" ")
        letter += 2
    else:
        for j in range(n):
            print("*", end=" ")
    print()


n = int(input("Enter number of letter rows: "))
letter = 97
for i in range(n * 2 - 1):
    if i % 2 == 0:
        ch = chr(letter)
        for j in range(n):
            print(ch, end=" ")
        letter += 2
    else:
        for j in range(n):
            print("*", end=" ")
    print()
n = int(input("Enter number of rows: "))
letter = 65 
for i in range(n):           
    temp = 65                   
    for j in range(n * 2 - 1): 
        if j % 2 == 0:
            print(chr(temp), end=" ")
            temp += 2
        else:
            print("*", end=" ")
    print()


n = int(input("Enter number of rows: "))
letter = 97
for i in range(n):           
    temp = 97                  
    for j in range(n * 2 - 1): 
        if j % 2 == 0:
            print(chr(temp), end=" ")
            temp += 2
        else:
            print("*", end=" ")
    print()

