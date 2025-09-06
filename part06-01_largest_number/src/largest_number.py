# write your solution here

def largest():
    """Reads 'numbers.txt' file containing integers and returns
    the biggest integer in the file."""

    with open("numbers.txt") as numbers:
        
        #transfer the numbers to a list and return the max.
        numbers_list = []
        for number in numbers:
            number = number.replace("\n","")
            numbers_list.append(int(number))
        return max(numbers_list)

if __name__ == "__main__":
    print(largest())
        
    


