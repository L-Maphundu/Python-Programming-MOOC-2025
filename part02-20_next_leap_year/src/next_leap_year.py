# Write your solution here

year = int(input("Please type in a year: "))

#Initial check if the entered year is not a leap year
next_year = year + 1
while True:
    if next_year % 4 != 0:                           #No year indivisible by 4 is a leap year.
        leap_year = False
    else:
        if next_year % 100 == 0 and next_year % 400 == 0: #For a year divisible by 100, check if it is divisible by 400.
            leap_year = True 
        elif next_year % 100 != 0:                   #All the years divible by 4 but not divisible by 400.
            leap_year = True 
        else:
            leap_year = False
    if leap_year:
        break
    next_year += 1
print(f"The next leap year after {year} is {next_year}")