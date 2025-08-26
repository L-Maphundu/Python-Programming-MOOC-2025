# Write your solution here
sentence = input("Please type in a sentence: ").strip()

for word in sentence.split():
    print(word[0])