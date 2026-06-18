#9.Rightangletriangle of alphabet A B B C C C D D D D E E E E E F F F F F F G G G G G G G H H H H H H H H I I I I I I I I I
n = int(input("Enter a number: "))
for i in range(1, n+1): 
    for j in range(1, i+1): 
        ch=(chr(64 +i))
        print(ch,end=" ")
    print()
#10. Rightangletriangle of alphabet A  A B  B  B C  C  C  C D  D  D  D  D E  E  E  E  E  E F  F  F  F  F  F  F G  G  G  G  G  G  G  G H H H H H H H H H
n = int(input("Enter a number: "))
for i in range(1, n+1): 
    for j in range(1, i+1): 
        ch=(chr(64 +j))
        print(ch,end=" ")
    print()
#11.Rightangletriangle of alphabet D CC BBB AAAA
n = int(input("Enter a number: "))
for i in range(n):  
    for j in range(i + 1):
        print(chr(68 - i), end=" ")
    print()
#12.Rightangletriangle of alphabet DDDD CCC BB A
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(68 - j), end=" ")
    print()
#13.Rightangletriangle of alphabet a b b c c c d d d d
n= int(input("Enter a number: "))
for i in range(1, n+1): 
    for j in range(1, i+1): 
        ch=(chr(96 +i))
        print(ch,end=" ")
    print()
#14. Rightangletriangle of alphabet a ab abc abcd 
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1): 
        ch=(chr(96 +j))
        print(ch,end=" ")
    print()
#15.Rightangletriangle of alphabet d cc bbb aaaa
n = int(input("Enter a number: "))
for i in range(n):  
    for j in range(i + 1):
        print(chr(100 - i), end=" ")
    print()
#16.Rightangletriangle of alphabet d dc dcb dcba
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(100 - j), end=" ")
    print()
#17.left angletriangle of alphabet a  bb ccc dddd
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(97 + i)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()
#18.left angletriangle of alphabet a a b  a b c  a b c d
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(97 + j), end=" ")
    print()
#19.left angletriangle of alphabet d cc bbb aaaa
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(97 + n - i - 1)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()
#20.left angletriangle of alphabet d dc dcb dcba
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(97 + n - j - 1), end=" ")
    print()
#21.Equalateral triangle of alphabet a bb ccc dddd
n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(97 + i)  
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(ch, end=" ")
    print()