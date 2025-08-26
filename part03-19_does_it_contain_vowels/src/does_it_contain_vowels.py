# Write your solution here
vowels = 'aeo'
string = input("Please type in a string: ").strip()

j = 0
while j < 3:
    if vowels[j] in string:
        print(f"{vowels[j]} found")
    else: 
        print(f"{vowels[j]} not found")
    j += 1