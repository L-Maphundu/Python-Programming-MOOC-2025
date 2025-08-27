# Write your solution here
words = []
while True:
    word = input("Word: ").strip()

    if word in words:
        break

    if word != "":
        words.append(word)
        
print(f"You typed in {len(words)} different words")