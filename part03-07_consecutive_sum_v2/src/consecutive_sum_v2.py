# Write your solution here
limit = input("Limit: ").strip()

if not limit.isnumeric():
    print("Not a valid number!")
else:
    limit = int(limit)
    tot = 0
    num = 1
    summation = "1"
    while tot < limit:
        tot += num
        if num > 1:
            summation += f" + {str(num)}"
        num += 1
    print(f"The consecutive sum: {summation} = {tot}")