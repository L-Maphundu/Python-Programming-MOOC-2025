# write your solution here
def matrix(file):
    """Reads a file that contains a matrix where each line represents
    each row of the matrix. Assumes the rows are of the same size and contain only integers. 
    Returns the matrix as a list."""
    matrix = []
    with open(file) as matrix_file:
        for row in matrix_file:
            row = (row.replace("\n","")).split(",")

            for i in range(len(row)): #Converts each element to int type for arithmetic operations
                row[i] = int(row[i])

            matrix.append(row)

    return matrix 

def matrix_sum():
    """Returns the sum of all the numbers in 'matrix.txt'."""
    tot = 0 
    for row in matrix('matrix.txt'):
        tot += sum(row)

    return tot

def matrix_max():
    """Returns the largerst number in the 'matrix.txt'."""
    largest = matrix('matrix.txt')[0][0]
    for row in matrix('matrix.txt'):
        for element in row:
            if element > largest:
                largest = element
    return largest


def row_sums():
    """Returns a list of each sum in 'matrix.txt'."""
    sums = []
    for row in matrix('matrix.txt'):
        sums.append(sum(row))
    return sums

if __name__ == "__main__":
    print(matrix('matrix.txt'))
    print()
    print(row_sums())        

