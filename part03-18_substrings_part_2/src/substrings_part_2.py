# Write your solution here
string = input("Please type in a string: ").strip()

for i in range(1, len(string) + 1):
    print(string[len(string)- i:])