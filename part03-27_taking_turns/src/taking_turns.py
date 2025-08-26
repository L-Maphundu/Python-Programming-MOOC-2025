# Write your solution here
number = int(input("Please type in a number: "))

count = 1
forward = 1
backward = number
while count <= number:
    if count % 2 != 0:
        print(forward)
        forward += 1
    else:
        print(backward)
        backward -= 1
    count += 1
