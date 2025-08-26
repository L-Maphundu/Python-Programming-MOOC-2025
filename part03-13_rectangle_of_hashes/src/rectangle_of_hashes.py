# Write your solution here
width = input("Width: ").strip()
height = input("Height: ").strip()

if width.isnumeric() and height.isnumeric():
    for i in range(int(height)):
        print("#"*int(width))
else:
    print("Please enter positive whole numbers for both width and height!")