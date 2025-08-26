# Write your solution here
num = int(input("Number: "))

message = ""
if num % 15 == 0:
    message = "FizzBuzz"
elif num % 5 == 0:
    message = "Buzz"
elif num % 3 == 0:
    message = "Fizz"
print(message)