# Write your solution here
def spruce(size):
    print("a spruce!")
    j = 1
    last = size 

    for i in range(size): #prints a triangle
        print(" "*(size - 1), "*"*j, sep="")
        j += 2
        size -= 1

    print(" "*(last - 1) + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)