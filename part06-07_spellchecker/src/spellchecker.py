# write your solution here
def word_list():
    """Reads the file wordlist.txt containing words 
    and returns a list containing the words."""
    
    words = []
    with open("wordlist.txt") as wordlist:
        for word in wordlist:
            word = word.strip()
            words.append(word)
    return words 

def spellchecker(text: str, wordlist: list):
    """Given a text, checks if every word is spelled correctly by comparing
    it to the wordlist provided and returns the text with incorred words highlighted.
    """
    checked = ""
    words = text.split(" ")
    for word in words:
        if word.lower() in wordlist:
            word = f"{word} "
        else:
            word = f"*{word}* "

        checked += word

    return checked.strip()


def main():
    text = input("Write text: ").strip()
    words = word_list()
    spellcheck = spellchecker(text, words)
    print(spellcheck)

main()


