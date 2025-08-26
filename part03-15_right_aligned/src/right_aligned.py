# Write your solution here
string = input("Please type in a string: ").strip()
if 20 - len(string) == 0:
    print(string)
else:
    print('*'*(20-len(string)) + string)
