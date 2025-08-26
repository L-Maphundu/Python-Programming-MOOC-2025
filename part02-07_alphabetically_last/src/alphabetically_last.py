# Write your solution here
word1 = input("Please type in 1st word: ").lower()
word2 = input("Please type in the 2nd word: ").lower()

if word1 == word2:
    print("You gave the same word twice")
else:
    print(f"{max(word1,word2)} comes alphabetically last.")