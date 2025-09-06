# write your solution here

def read_fruits():
    """Reads 'fruits.csv' file and returns a dictionary (data)
    of fruit names (keys) and prices (values). Each line
    in the file is a fruit and its price."""

    with open("fruits.csv") as fruits:

        data = {}        
        for fruit in fruits:
            fruit = (fruit.replace("\n","")).split(";")
            data[fruit[0]] = float(fruit[1])
    return data

if __name__ == "__main__":
    print(read_fruits())