# Write your solution here
def enter_entry(text: str):
    """Records diary entries of the user into
    diary.txt"""
    with open("diary.txt", "a") as diary:
        diary.write(f"{text}\n")

def read_entries():
    """Reads diary entries from diary.txt."""
    with open("diary.txt") as diary:
        entries = diary.read()
        print(entries)

def main():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        option = input("Function: ").strip()
    
        #Silently handles invalid entries since the loop terminates only with '0'.
        if option == "0":
            break

        elif option == "1":
            text = input("Diary entry: ").strip()
            enter_entry(text)
            print("Diary saved")

        elif option == "2":
            print("Entries:")
            read_entries()
    print("Bye now!")

main()