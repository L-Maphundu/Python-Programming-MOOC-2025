# Write your solution here
def anagrams(string1,string2):
    if len(string1) != len(string2):
        return False

    for char in string1:
        if char not in string2:
            return False
            
    return True

if __name__ == "__main__":
    print(anagrams('tree','three'))