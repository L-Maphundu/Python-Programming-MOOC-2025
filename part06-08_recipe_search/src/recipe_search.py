# Write your solution here
def search_by_name(filename: str, word: str):
    """Takes in a file containing recipes and a word to search for
    in the recipe names in the file and returns a list of recipe
    names containing the word.
    """

    names = []
    with open(filename) as recipes:
        for line in recipes:
            if word.lower() in line.lower():
                names.append(line.strip())


    return names

def main():
    word = "cake" #input("Enter food name: ")
    filename = "recipes1.txt" #input("Enter file name: ")
    recipe_names = search_by_name(filename, word)

    for name in recipe_names:
        print(name)

main()

