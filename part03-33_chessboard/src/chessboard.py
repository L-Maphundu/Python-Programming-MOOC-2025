# Write your solution here
def chessboard(num):

    for i in range(1, num + 1):
        if i % 2 != 0:
            one = '1'
            zero = '0'
        else:
            one = '0'
            zero = '1'

        for j in range(1, num +1):
            if j % 2 != 0:
                print(one,end="")
            else:
                print(zero,end="")
        print()

            


# Testing the function
if __name__ == "__main__":
    chessboard(3)
