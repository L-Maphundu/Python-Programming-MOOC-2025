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