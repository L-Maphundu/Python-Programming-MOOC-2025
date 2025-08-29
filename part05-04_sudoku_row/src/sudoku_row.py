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

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))