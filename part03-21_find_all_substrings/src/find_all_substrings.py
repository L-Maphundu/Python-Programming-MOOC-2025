# Write your solution here
word = input("Please type in a word: ").strip()
character = input("Please type in a character: ").strip()

while True:
    index = word.find(character) #This will be the starting index for the substring if it is 3 characters long. 
    limit = index + 3 #This must always be less than or equal to the length of the word
    if index != -1 and limit <= len(word):
        print(word[index:limit])
        word = word[index + 1:] #Updates the word by deleting the current occurance of the character.
    else:
        break  