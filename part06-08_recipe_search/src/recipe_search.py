# Write your solution here
def search_by_name(filename: str, word: str):
    """Takes in a file containing recipes and a word to search for
    in the recipe names in the file and returns a list of recipe
    names containing the word.
    """

    names = []
    lines = []
    with open(filename) as recipes:
        for line in recipes:
            lines.append(line)
            index = len(lines) - 2
            if word.lower() in line.lower() and (len(lines) == 1 or lines[index] == "\n"): 
                #Avoids cases where the search word is found but not in the name but as ingredient.
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

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)

