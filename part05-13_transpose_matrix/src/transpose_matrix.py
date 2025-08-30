# Write your solution here
def transpose(matrix: list):
    """Transposes any given square matrix."""
    
    copy = matrix[:]
    for i in range(len(matrix)):
        copy[i] = (matrix[i])[:]
    
    row_no = 0 #row number of original matrix
    while row_no**2 <= (len(matrix) - 1)**2:   
        for column_no in range(len(matrix[row_no])):
            matrix[row_no][column_no] = copy[column_no][row_no]
        row_no += 1

    del copy
    print(matrix)

if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print("original")
    print(matrix)        
    transpose(matrix)
