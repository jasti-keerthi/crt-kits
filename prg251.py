#65.combinations of number and stars 1*** 22** 3333* 4444
n = 4
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(i, end=" ")
        else:
            print("*", end=" ")
    print()
print("------------------------")

#66.combinations of number and stars 1*** 12** 123* 1234
n = 4
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:
            print(j, end=" ")
        else:
            print("*", end=" ")
    print()
print("------------------------------------")
#67.equalateral triangle of alphabets a bbb ccccc dddddd
n = 4
for i in range(n):
    print(" " * (n - i - 1), end="")
    print(chr(97 + i) * (2 * i + 1))
print("--------------------------------")
#68.equalateral triangle of alphabets a aba abcbc abcdcba
n = 4

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(97 + j), end="")
    for j in range(i - 2, -1, -1):
        print(chr(97 + j), end="")
    print()
print("----------------------")

