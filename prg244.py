#1.square of alphabet AAAAA BBBBB CCCCC DDDDD EEEEE FFFFFF GGGGGGG HHHHHHHH IIIIIIIII JJJJJJJJJJ KKKKKKKKKKK LLLLLLLLLLLL MMMMMMMMMMMMM NNNNNNNNNNNN OOOOOOOOOOOOO PPPPPPPPPPPPP QQQQQQQQQQQQQ RRRRRRRRRRRRRR SSSSSSSSSSSSSS TTTTTTTTTTTTTT UUUUUUUUUUUUUU VVVVVVVVVVVVVV WWWWWWWWWWWWWWW XXXXXXXXXXXXXXX YYYYYYYYYYYYYYYY ZZZZZZZZZZZZZZZZ
n = int(input("Enter a number: "))
for i in range(1, n+1): 
    for j in range(1, n+1): 
        ch=(chr(64 +i))
        print(ch,end=" ")
    print()

#2.square of alphabet AAAA BBBBB CCCCC DDDDD EEEEE FFFFFF GGGGGGG HHHHHHHH IIIIIIIII JJJJJJJJJJ KKKKKKKKKKK LLLLLLLLLLLL MMMMMMMMMMMMM NNNNNNNNNNNN OOOOOOOOOOOOO PPPPPPPPPPPPP QQQQQQQQQQQQQ RRRRRRRRRRRRRR SSSSSSSSSSSSSS TTTTTTTTTTTTTT UUUUUUUUUUUUUU VVVVVVVVVVVVVV WWWWWWWWWWWWWWW XXXXXXXXXXXXXXX YYYYYYYYYYYYYYYY ZZZZZZZZZZZZZZZZ
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(n,0,-1):
        ch=(chr(64 +i))
        print(ch,end=" ")
    print()
#3.square of alphabet A B C D A B C D A B C D A B C D A B C D
n = int(input("Enter a number: "))  
for i in range(1, n+1): 
    for j in range(1, n+1): 
        ch=(chr(64 +j))
        print(ch,end=" ")
    print()
#4.square of alphabet D C B A D C B A D C B A D C B A
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(n,0,-1):
        ch=(chr(64 +j))
        print(ch,end=" ")
    print()
#5.square of alphabet  aaaa bbbb cccc dddd eeee ffff gggg hhhh iiii jjjj kkkk llll mmmm nnnn oooo pppp qqqq rrrr ssss tttt uuuu vvvv wwww xxxx yyyy zzzz
n = int(input("Enter a number: "))  
for i in range(1, n+1): 
    for j in range(1, n+1): 
        ch=(chr(96 +i))
        print(ch,end=" ")
    print()
#6.square of alphabet zzzz yyyy xxxx wwww vvvv uuuu tttt ssss rrrr qqqq pppp oooo nnnn mmmm llll kkkk jjjj iiii hhhh gggg ffff eeee dddd cccc bbbb aaaa
n = int(input("Enter a number: "))  
for i in range(n, 0, -1):
    for j in range(n,0,-1):
        ch=(chr(96 +i))
        print(ch,end=" ")
    print()
#7.square of alphabet a b c d a b c d a b c d a b c d a b c d
n = int(input("Enter a number: "))  
for i in range(1, n+1): 
    for j in range(1, n+1): 
        ch=(chr(96 +j))
        print(ch,end=" ")
    print()
#8.square of alphabet d c b a d c b a d c b a d c b a d c b a
n = int(input("Enter a number: "))  
for i in range(n, 0, -1):
    for j in range(n,0,-1):
        ch=(chr(96 +j))
        print(ch,end=" ")
    print()
