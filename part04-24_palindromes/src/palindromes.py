# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(string1):
    return string1 == string1[::-1]

def main():
    while True:
        word = input("Please type in a palindrome: ").strip()
        if palindromes(word):
            break
        print("that wasn't a palindrome")
    print(word, "is a palindrome!")

main()
