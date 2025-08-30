# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    copy = sudoku[:]

    row_copy = (sudoku[row_no])[:]
    row_copy[column_no] = number 

    copy[row_no] = row_copy


    return copy

