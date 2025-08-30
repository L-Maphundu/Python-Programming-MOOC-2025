# Write your solution here
def double_items(numbers: list):
    copy = numbers[:]

    for i in range(len(copy)):
        copy[i] *= 2
        
    return copy

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)   