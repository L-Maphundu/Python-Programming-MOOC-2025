# Write your solution here
limit = int(input("Upper limit: "))
base = int(input("Base: "))
power = 0
try:
    while base**power <= limit:
        print(base**power)
        power += 1
except:
    print("Base or power invalid!")