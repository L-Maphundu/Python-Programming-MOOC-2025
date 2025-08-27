# Write your solution here
def no_vowels(string):
    string1 = ""
    for char in string:
        if char not in 'aeiou':
            string1 += char
            
    return string1