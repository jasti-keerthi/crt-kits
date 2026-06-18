#50.square pattern of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65 
for i in range(n):
    for j in range(n):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#51.square pattern of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(n):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#53.rigtangle triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#54.rigtangle triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#55.downward triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#56.downward triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#57.left angle triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#58.left angle triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#59.downward left angle triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4 
ch = 65
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#60.downward left angle triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#61.downward equalateral triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")

#62.downward equalateral triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")
#63.equalateral triangle of alphabet a b c d e f g h i j k l m n o p q r s t u v w x y z
n=4
ch = 97
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")
#64.equalateral triangle of alphabet A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
n=4
ch = 65
for i in range(n):  
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("--------------------------------")
