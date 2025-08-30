# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    """Places the given piece at the given coordinates on the board(3x3 matrix).
    y is the row numer and x the column number. Assumes the player
    will always enter an integer."""

    if not (0<=x<=2) or not (0<=y<=2) or not (game_board[y][x] == ""):
        return False
    
    game_board[y][x] = piece
    return True

if __name__ == "__main__":
    game_board = [['O', 'O', 'O'], ['O', '', ''], ['', 'X', 'X']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)