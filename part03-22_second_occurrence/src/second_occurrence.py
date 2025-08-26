# Write your solution here
word = input("Please type in a word: ").strip()
substring = input("Please type in a substring: ").strip()

occurance = 0 #counts the number of occurances of the substring up to 2.

while True:
    index = word.find(substring)    #This will be the starting index of the substring. 
    limit = index + len(substring)    
    
    if index > -1:
        occurance += 1
        if occurance == 2:      #The final index is the length of the deleted string plus the index of the 2nd occurrence in the shortened word.
            print(f"The second occurrence of the substring is at index {len(deleted_substring) + index}.")
            break
        deleted_substring = word[:limit]
        word = word[limit:]     #Updates the word to avoid overlap.
    else:
        print("The substring does not occur twice in the string.")
        break

