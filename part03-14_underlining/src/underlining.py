# Write your solution here

while True:
    string = input("Please type in a string: ").strip()
    if len(string) < 1:
        break
    
    print(string)
    print(len(string)*"-")
        