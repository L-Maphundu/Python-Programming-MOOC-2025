# Write your solution here
def search_by_name(filename: str, word: str):
    """Takes in a file containing recipes and a word to search for
    in the recipe names and returns a list of all the recipe
    names containing the word.
    """

    names = []
    recipe = []
    with open(filename) as recipes_data:
        for line in recipes_data:
            line = line.strip()
            recipe.append(line) 

            if line == "": #This is the end of a recipe in the file.
                recipe = []
                continue

            if word.lower() in line.lower() and len(recipe) == 1: 
                #Avoids cases where the search word is found but not in the name but in ingredient.
                names.append(line)

    return names

def search_by_time(filename: str, prep_time: int):
    """Takes in a file containing recipes and preparation time to search for
    and returns a list of all the recipes that match the preparation time or take 
    less time to prepare.
    """

    results = []
    recipe = []
    with open(filename) as recipes_data:
        for line in recipes_data:
            line = line.strip()

            if line == "": #An empty line signifies the end of a recipe
                recipe = []
                continue

            recipe.append(line)
            if line.isnumeric() and int(line) <= prep_time:
                results.append(f"{recipe[0]}, preparation time {line} min")
                recipe = []

    return results

def search_by_ingredient(filename: str, ingredient: str):
    """Takes in a file containing recipes and an igredient to search for
    and returns a list of all recipes that contain the ingredient."""
    results = []
    recipe = []
    with open(filename) as recipes:
        for line in recipes:
            line = line.strip()

            if line == "": #An empty line signifies the end of a recipe
                recipe = []
                continue

            recipe.append(line)
            if ingredient.lower() in line.lower() and (len(recipe) > 1): 
                results.append(f"{recipe[0]}, preparation time {recipe[1]} min")
                recipe = []

    return results

if __name__ == "__main__":
    found_recipes = search_by_time("recipes1.txt", 35)
    for recipe in found_recipes:
        print(recipe)

