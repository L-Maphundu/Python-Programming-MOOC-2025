# Write your solution here
def longest_series_of_neighbours(list):

    neighbours = [list[0]]
    longest = 0

    for num in list:
        if abs(num - neighbours[-1]) == 1:
            neighbours.append(num)
            if len(neighbours) > longest:
                longest = len(neighbours)
        else:
            neighbours = [num]
            
    return longest

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list)) #4