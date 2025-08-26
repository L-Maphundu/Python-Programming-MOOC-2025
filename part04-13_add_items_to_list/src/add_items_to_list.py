# Write your solution here
items = int(input("How many items: "))
list = []

count = 1

while count <= items:
    item = int(input(f"item{count}: ").strip())
    list.append(item)
    count += 1

print(list)