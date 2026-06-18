#33.downward triangle of alphabet DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    print("  " * i, end=" ")          
    for j in range(n - i):
        print(chr(68 - i) , end=" ")
    print()
#34.downward triangle of alphabet ABCD ABC AB A
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")  
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    print()
#35.downward triangle of alphabet AAAA BBB CC D
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")           
    for j in range(n - i):
        print(chr(65 + i) , end=" ")
    print()
#36.downward triangle of alphabet DCBA DCB DC D
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")  
    for j in range(n - i):
        print(chr(68 - j), end=" ")
    print()
#37.downward triangle of alphabet aaaa bbb cc d
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")           
    for j in range(n - i):
        print(chr(97 + i) , end=" ")
    print()
#38.downward triangle of alphabet dcba dcb dc d
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")  
    for j in range(n - i):
        print(chr(97 + n - j - 1), end=" ")
    print()
#39.downward triangle of alphabet abcd abc ab a
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")  
    for j in range(n - i):
        print(chr(97 + j), end=" ")
    print()
#40.downward triangle of alphabet dddd ccc bb a
n = int(input("Enter a number: "))
for i in range(n):  
    print("  " * i, end=" ")           
    for j in range(n - i):
        print(chr(97 + n - i - 1) , end=" ")
    print()