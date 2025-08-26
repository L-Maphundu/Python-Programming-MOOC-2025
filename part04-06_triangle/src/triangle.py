# Copy here code of line function from previous exercise
def line(num, string):
    if string == '':
        string = '*'
    else:
        string = string[0]
    print(string*num)

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(1, size + 1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
