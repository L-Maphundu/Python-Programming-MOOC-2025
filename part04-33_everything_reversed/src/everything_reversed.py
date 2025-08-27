# Write your solution here
def everything_reversed(list):
    list = list[::-1]
    for i in range(len(list)):
        list[i] = list[i][::-1]
    return list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
