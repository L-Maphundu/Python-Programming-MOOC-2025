# Write your solution here
def sum_of_positives(list):
    tot = 0
    for num in list:
        if num > 0:
            tot += num
    return tot

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
