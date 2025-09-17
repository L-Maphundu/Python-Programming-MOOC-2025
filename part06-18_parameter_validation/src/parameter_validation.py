# Write your solution here
def new_person(name: str, age: int):
    """Returns a tuple of name and age received as first
    and second parameter respectively."""

    name = name.strip()
    error1 = (name == "") or not ( (len(name.split(" ")) >= 2 and len(name) <= 40) ) #Assume for "A B" counts as two words making up a name
    error2 = not (0 < age <= 150)
   
    if error1 or error2 :
        raise ValueError(
            """Please check if none of these occured:
            name is an empty string
            name contains less than two words
            name is longer than 40 characters
            age is a negative number
            age is greater than 150"""
        )
    else:
        return (name, age)

if __name__ == "__main__":
    print(new_person("Steve Biko", -1 ))
