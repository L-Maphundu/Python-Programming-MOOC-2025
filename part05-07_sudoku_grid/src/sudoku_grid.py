# Write your solution here
def row_correct(sudoku: list, row_no: int):
    """Checkers if the given row does not contain the same number
    twice for numbers 1-9."""

    numbers = [x for x in range(1,10)]
    row = sudoku[row_no]
  
    for number in numbers:
        count = 0
        for entry in row:
            if entry == number:
                count += 1
        if count > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    """Checks if a numbers 1-9 appear only once in a column
    of a given matrix (sudoku)"""

    numbers = []

    for row in sudoku:
        if row[column_no] != 0 and row[column_no] in numbers:
            return False
        numbers.append(row[column_no])
    
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    """Checks if a number from 1-9 is not repeated in a 3x3 matrix
    taken from a bigger nxn matrix"""

    numbers = []
    entries = []

    for i in range(row_no, row_no + 3):
        entries += (sudoku[i])[column_no: (column_no + 3)]
    
    for number in entries:
        if number != 0 and number in numbers:
            return False
        numbers.append(number)

    return True

def sudoku_grid_correct(sudoku: list):
    #first we check the rows and columns together, if they fail no need to check 3x3 blocks.
    for i in range (9):
        if not (column_correct(sudoku,i) and row_correct(sudoku,i)):
            return False
    
    #Now we check the 3x3 blocks
    row_no = 0
    while row_no < 7:
        for column_no in range(0,7,3):
            if not block_correct(sudoku, row_no, column_no):
                return False

        row_no += 3

    return True


