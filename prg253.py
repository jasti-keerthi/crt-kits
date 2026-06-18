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

#79.reacple the word with asterisks
sentence = input("Enter a sentence: ")
target = input("Enter the target word: ")
result = sentence.replace(target, "*" * len(target))
print(result)
print("--------------------------")

#80.count of non palindromes.
sentence = input("Enter a sentence: ")
words = sentence.split()
count = 0
for word in words:
    if word.lower() != word[::-1].lower():
        count += 1
print("Count of non-palindrome words:", count)