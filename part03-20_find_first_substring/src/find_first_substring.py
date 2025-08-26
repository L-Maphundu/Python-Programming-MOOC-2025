# Write your solution here
#Assumes the input is at least 3 characters long.

word = input("Please type in a word: ").strip()
character = input("Please type in a character: ").strip()

index = word.find(character)
limit = index + 3

if index != -1 and limit < len(word):
    print(word[index:limit])