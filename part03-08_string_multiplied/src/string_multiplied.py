# Write your solution here
word = input("Please type in a string: ").strip()
amount = input("Please type an amount: ")

if not amount.isnumeric():
    print("Please enter a valid number!")
else:
    print(word*int(amount))