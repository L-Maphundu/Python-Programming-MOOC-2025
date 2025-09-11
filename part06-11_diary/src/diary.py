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
        if option not in ["0", "1", "2"]: #Silently handles invalid entries. Not specified from spec but not a bad deviation.
            continue
        
        #The error handling above guarantees option will eventually be 0, 1 or 2.
        if option == "0":
            break

        elif option == "1":
            text = input("Diary entry: ").strip()
            enter_entry(text)
            print("Diary saved")

        else:
            print("Entries:")
            read_entries()
    print("Bye now!")
main()