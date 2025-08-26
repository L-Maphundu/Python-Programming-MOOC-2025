# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(num, string):
    if string == '':
        string = '*'
    else:
        string = string[0]
    print(string*num)

def shape(size1,char1,size2,char2):
    for i in range(1, size1 + 1):
        line(i,char1)
    for i in range(size2):
        line(size1,char2)

if __name__ == "__main__":
    shape(5, "x", 2, "o")