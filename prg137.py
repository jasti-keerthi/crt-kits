msg = input("Enter message: ")
n = int(input("Enter number of banned words: "))

for i in range(n):
    word = input("Enter banned word: ")
    msg = msg.replace(word, "*" * len(word))

print("Filtered Message:", msg)