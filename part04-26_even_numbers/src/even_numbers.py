# Write your solution here
def even_numbers(list):
    evens = []
    for num in list:
        if num % 2 == 0:
            evens.append(num)
    return evens