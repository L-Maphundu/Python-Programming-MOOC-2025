# Write your solution here
list = []

while True:
    print(f"The list is now {list}")
    choice = input("a(d)d, (r)emove or e(x)it: ").strip().lower()

    if choice == "x":
        break

    if choice == "d":
        if list == []:
            list.append(1) #initialize the list.
        else:
            list.append(list[-1] + 1)
    else:
        list.remove(list[-1])
    

print("Bye!")