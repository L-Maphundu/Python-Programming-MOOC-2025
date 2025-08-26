# Write your solution here
#"You can assume all given index values will fall within your list."

list = [x for x in range(1,6)]
while True:
    index = int(input("Index: ").strip())
    
    if index == -1:
        break
    new_value = int(input("New value: ").strip())
    list[index] = new_value
    print(list)