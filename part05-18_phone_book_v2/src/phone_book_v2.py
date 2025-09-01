# Write your solution here
phonebook = {}

while True:
    option = input("command (1 search, 2 add, 3 quit): ").strip()

    if option == "3":
        print("quitting...")
        break

    elif option == "1":
        name = input("name: ").strip().lower()
        if name in phonebook:
            for number in phonebook[name]:
                print(number)
        else:
            print("no number")

    elif option == "2":
        name = input("name: ").strip().lower()
        number = input("number: ").strip().lower()
        if name in phonebook:
            phonebook[name].append(number)        
        else:
            phonebook[name] = [number]
        print("ok!")

    else:
        print("Please enter 1, 2 or 3!")