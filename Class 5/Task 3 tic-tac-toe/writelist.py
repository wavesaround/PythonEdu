import valid

def init(board: list, user: int) -> list:
    user_type = valid.init(2)
    if user == 1:
        board[user_type - 1] = 'X'
        return board
    elif user == 2:
        board[user_type - 1] = 'O'
        return board