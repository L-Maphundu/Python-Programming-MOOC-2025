# Write your solution here
def word_list():
    """Reads the 'words.txt' file which contains English
    words and returns the words as a list."""
    word_list = []
    with open("words.txt") as words:
        for word in words:
            word = word.strip()
            word_list.append(word)
    return word_list

def asterik(search_term: str, words: list):
    """Returns a list of all the """
    results = []
    search_term = search_term.lower()

    if search_term.endswith('*'):
        search_term = search_term[:-1]
        for word in words:
            if word.startswith(search_term):
                results.append(word)

    elif search_term.startswith('*'):
        search_term = search_term[1:]
        for word in words:
            if word.endswith(search_term):
                results.append(word)

        return results

def find_words(search_term: str):
    """Returns a list of all the words in word_list()
    that match the search term based on wildcards '.' and '*'."""
    words = word_list()

    if '*' in search_term:
        return asterik(search_term, words)
        
def main():
    print(find_words("*vokes"))

main()