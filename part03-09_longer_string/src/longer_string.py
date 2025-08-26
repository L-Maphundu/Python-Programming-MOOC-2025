# Write your solution here
word1 = input("Please type in string 1: ").strip()
word2 = input("Please type in string 2: ").strip()

if len(word1) == len(word2):
    print("The strings are equally long")
elif len(word2) > len(word1):
    print(f"{word2} is longer")
else:
    print(f"{word1} is longer")