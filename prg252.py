#example of word pattern
n="Hello"
for i in range(len(n)):
    for j in range(len(n)):
        print(n[i], end=" ")
    print()
print("-----------------")

#69. square Word pattern
n = "python"
for i in range(len(n)):
    for j in range(len(n)):
        print(n[i], end=" ")
    print()
print("------------------------------")

#70.rigth angel triangel of word pattern
n = "python"
for i in range(len(n)):
    for j in range(i + 1):
        print(n[j], end=" ")
    print()
print("---------------------------")

#71.rigthangle triangle of word pattern p yy ttt hhhh ooooo nnnnnn
n = "python"
for i in range(len(n)):
    for j in range(i + 1):
        print(n[i], end=" ")
    print()
print("--------------------------")

#72.square of python
n = "python"
rev = n[::-1]
for ch in rev:
    for i in range(len(n)):
        print(ch, end=" ")
    print()
print("-------------------------")

#73.downwrd triagnle of word pattern 
n = "python"
for i in range(len(n), 0, -1):
    for j in range(i):
        print(n[j], end=" ")
    print()
print("-----------------------------------")

#74.right angle triangle of a word pattern
n = "python"
for i in range(1, len(n) + 1):
    for j in range(i):
        print(n[j], end=" ")
    print()
print("--------------------------------")

#75.downward triangle of word pattern
word = "python"
rev = word[::-1]   # python -> nohtyp
n = len(rev)
for i in range(n):
    for j in range(n - i):
        print(rev[i], end=" ")
    print()

#76.downward left angle triangle of word pattern
word = "python"
n = len(word)
for i in range(n):
    print("  " * i, end="")
    for j in range(i, n):
        print(word[j], end=" ")
    print()
print("-------------------------")

#77.palindrom words in a sentence 
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    if word.lower() == word.lower()[::-1]:
        print(word)
print("-------------------------------")

#78.convert normal sentence to snake_case
sentence = input("Enter a sentence: ")
snake_case = sentence.lower().replace(" ", "_")
print(snake_case)
print("-----------------------------")