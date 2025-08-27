# Write your solution here
def distinct_numbers(list):
    distinct = []
    for num in list:
        if num not in distinct:
            distinct.append(num)
    return sorted(distinct)