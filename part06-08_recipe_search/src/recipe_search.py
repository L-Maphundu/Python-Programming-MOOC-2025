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

def search_by_time(filename: str, prep_time: int):
    #Pancakes, preparation time 15 min
    results = []
    recipes = []
    with open(filename) as recipes_data:
        for line in recipes_data:
            line = line.strip()
            recipes.append(line)
            if line.isnumeric() and int(line) <= prep_time:
                results.append(f"{recipes[-2]}, preparation time {line} min")
    return results

def main():
    word = "cake" #input("Enter food name: ")
    prep_time = 20
    filename = "recipes1.txt" #input("Enter file name: ")
    recipe_names = search_by_name(filename, word)
    recipe_times = search_by_time(filename, prep_time)

    for name in recipe_times:
        print(name)

main()

