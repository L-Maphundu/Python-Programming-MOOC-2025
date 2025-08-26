# Write your solution here
year = int(input("Please type in a year: "))

if year % 4 != 0:                           #No year indivisible by 4 is a leap year.
    message = "That year is not a leap year." 
else:
    if year % 100 == 0 and year % 400 == 0: #For a year divisible by 100, check if it is divisible by 400.
        message = "That year is a leap year."
    elif year % 100 != 0:                   #All the years divible by 4 but not divisible by 400.
        message = "That year is a leap year."
    else:
        message = "That year is not a leap year."


print(message)
    