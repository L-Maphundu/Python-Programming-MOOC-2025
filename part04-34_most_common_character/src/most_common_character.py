# Write your solution here
def most_common_character(string):
    count = 0
    highest = ""

    for char in string:
        if string.count(char) > count:
            count = string.count(char)
            highest = char
            
    return highest
