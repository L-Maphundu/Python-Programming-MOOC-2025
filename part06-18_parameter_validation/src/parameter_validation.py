# Write your solution here
def new_person(name: str, age: int):
    """Retunrs a tuple of name and age received as first
    and second parameter respectively."""
    
    name = name.strip()
    error1 = (name == "") or not ((2 <= len(name) <= 40) and (" " in name) ) #Assume for "A B" counts as two words making up a name
    error2 = not (0 < age <= 150)
   
    if error1 or error2 :
        raise ValueError("Something went wrong.")
    else:
        return (name, age)

if __name__ == "__main__":
    print(new_person("luyolo Maphundu", 32))
