# Write your solution here
list = []
while True:
    num = int(input("New item: ").strip())

    if num == 0:
        print("Bye!")
        break
    list.append(num)
    print("The list now:", list)
    print("The list in order:",sorted(list))

