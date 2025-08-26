# Write your solution here
story = ""
previous_word = ""
while True:
    
    word = input("Please type in a word: ")

    if word.lower() == "end" or word == previous_word:
        break
    else:
        previous_word = word
    story += word + " "
    

print(story)