# Write your solution here
def read():
    """Reads the contents of 'dictionary.txt'
    and returns a dictionary. The contents are
    pairs of Finnish words and their English
    translations."""
    dictionary = {}
    with open("dictionary.txt") as entries:
        for entry in entries:
            entry = entry.strip()
            finnish, english  = entry.split(":")
            dictionary[finnish] = english
    return dictionary

def entries(finnish_word: str, english_translation: str):
    """Adds a word and its definition to 'dictionary.txt'
    where the word and its definition are seperated by ':'.
    When adding a new word, you always start with the Finnish
    word and then add its English translation."""
    entries = read()

    if finnish_word not in entries:
        with open("dictionary.txt", "a") as dictionary:
            dictionary.write(f"{finnish_word}:{english_translation}\n")

def search(word: str):
    """Given an English or Finnish word, searchers for all
    Finnish or English translations that contain the word respectively ."""
    dictionary = read()
    for finnish_word, english_word in dictionary.items():
        if word in finnish_word or word in english_word:
            print(f"{finnish_word} - {english_word}")

def main():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        option = input("Function: ").strip()

        if option == "3":
            break
        elif option == "2":
            word = input("Search term: ").strip().lower()
            search(word)
        elif option == "1":
            word = input("The word in Finnish: ").strip()
            translation = input("The word in English: ").strip()
            entries(word, translation)
            print("Dictionary entry added")

    print("Bye!")
    
main()
