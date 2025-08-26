# Write your solution here
width = input("Width: ").strip()
if width.isnumeric():
    print("#"*int(width))
else:
    print("Please enter a positive number!")