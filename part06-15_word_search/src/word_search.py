# Write your solution here
def word_list():
    """Reads the words.txt file which contains English
    words and returns the words as a list."""
    word_list = []
    with open("words.txt") as words:
        for word in words:
            word = word.strip()
            word_list.append(word)
    return word_list

def find_words(search_term: str):
    pass

def main():
    print(word_list())

main()