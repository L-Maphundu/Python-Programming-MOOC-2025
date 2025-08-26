# Write your solution here
"""
limit = int(input("Upper limit: "))
base = 2
exponent = 0
while base**exponent <= limit:
    print(base**exponent)
    exponent += 1
"""




limit = int(input("Upper limit: "))
for i in range(limit):
    
    if 2**i > limit:
        break
    print(2**i)


