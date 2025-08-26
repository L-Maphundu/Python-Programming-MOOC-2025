# Write your solution here
print("Person 1: ")
name1 = input("Person 1: ")
age1 = int(input("Age: "))

print("Person 2: ")
name2 = input("Person 2: ")
age2 = int(input("Age: "))

if age1 == age2:
    print(f"{name1} and {name2} are the same age")
elif age1 > age2:
    print("The elder is", name1)
else:
    print("The elder is", name2)
