#25.Equalateral triangle of alphabet a bb ccc dddd
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(96 + i), end=" ")
    print()
#26.Equalateral triangle of alphabet a a b  a b c  a b c d
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(96 + j), end=" ")
    print()
#27.Equalateral triangle of alphabet d cc bbb aaaa
n = int(input("Enter a number: "))  
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(96 + n - i), end=" ")
    print()
#28.Equalateral triangle of alphabet d dc dcb dcba
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(96 + n - j), end=" ")
    print()
#29.Equalateral triangle of alphabet A BB CCC DDDD
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + i), end=" ")
    print()
#30.Equalateral triangle of alphabet A A B  A B C  A B C D
n = int(input("Enter a number: "))  
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()
#31.Equalateral triangle of alphabet D CC BBB AAAA
n = int(input("Enter a number: "))  
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(68 - i), end=" ")
    print()
#32.Equalateral triangle of alphabet DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(68 - j), end=" ")
    print()
#33.Equalateral triangle of alphabet DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(68 - j), end=" ")
    print()