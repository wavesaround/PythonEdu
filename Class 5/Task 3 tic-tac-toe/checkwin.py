
def init(board: list, user: int) -> bool:
    if user == 1: char = 'X'
    else: char = 'O'
    def check(char):
        if (((board[0] == board[1] == board[2])) or
            ((board[3] == board[4] == board[5])) or
            ((board[6] == board[7] == board[8])) or
            ((board[0] == board[4] == board[8])) or
            ((board[2] == board[4] == board[6])) or
            ((board[3] == board[4] == board[5])) or
            ((board[0] == board[3] == board[6])) or
            ((board[1] == board[4] == board[7])) or
            ((board[2] == board[5] == board[8])) 
        ):
            return True
        else: return False
    return check(char)