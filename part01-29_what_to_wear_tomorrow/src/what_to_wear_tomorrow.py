# Write your solution here
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ").lower()

if temp <= 5:
    print('Wear jeans and a T-shirt', 'I recommend a jumper as well', sep='\n')
    print('Take a jacket with you', 'Make it a warm coat, actually', sep='\n')
    print('I think gloves are in order')
elif 5 < temp <= 10:
    print('Wear jeans and a T-shirt', 'I recommend a jumper as well', sep='\n')
    print('Take a jacket with you')
elif 10 < temp <= 20:
    print('Wear jeans and a T-shirt', 'I recommend a jumper as well', sep='\n')
else: print('Wear jeans and a T-shirt')

if rain == 'yes': print("Don't forget your umbrella!")
