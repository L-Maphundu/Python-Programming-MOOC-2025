# Write your solution here

"""initializes the variables that will be needed at the end to print out
statistics"""
print("Please type in integer numbers. Type in 0 to finish.")
total = 0       #The sum of the numbers the user will enter
mean = 0        #The average of the numbers
positive = 0    #Number of positive numbers entered
negative = 0    #Number of negative numbers entered
while True:
    number = int(input("Number: "))

    if number == 0:
        break
    elif number > 0:
        positive += 1
    else:
        negative += 1
    total += number
    mean = total/(positive + negative)
print()   
print(f"Numbers typed in {positive+negative}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {mean:.1f}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")