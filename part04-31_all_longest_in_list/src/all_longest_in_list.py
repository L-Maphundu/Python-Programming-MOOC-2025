# Write your solution here
def all_the_longest(list):
    longest = ""
    long = []
    for word in list:
        if len(word) >= len(longest):
            if len(word) > len(longest):
                long = []
                longest = word
            long.append(word)

    return long
    
if __name__ == "__main__":
    my_list = ['Alan', 'Steve', 'Seymour', 'Kim', 'Susan']
    print()
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
    print()
