# Write your solution here

while True:
    try:
        number = int(input("Please type in a number: "))
        if number > 0:
            factorial = 1
            for i in range(1,number + 1):
                factorial *= i
            print(f"The factorial of the number {number} is {factorial}")
        else:
            print("Thanks and bye!")
            break
                
    except ValueError:
        print("Invalid! Please enter a numerical value.")
