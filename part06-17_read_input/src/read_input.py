# Write your solution here
def read_input(prompt: str, lower_bound, upper_bound):
    while True:
        try:
            num = int(input(f"{prompt}").strip())

        except:
            num = upper_bound + 1 #
        
        if lower_bound <= num <= upper_bound:
            return num
        else:
            print("You must type in an integer")
        

def main():
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)

main()
