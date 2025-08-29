# Write your solution here
def longest(list):

    longest = ""
    length = 0

    for string in list:
        if len(string) > length:
            longest = string
            length = len(string)
    return longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

        
