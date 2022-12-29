def board(board):
    print("-" * 19)
    for i in range(3):
        print("| ", board[0+i*3], " | ", board[1+i*3]," | ", board[2+i*3], " | ")
        print("–" * 19)

def go(switch: int):
    if switch == 1:
        print()
        print('Игрок 1, у вас (X), введите номер ячейки', end=' --> ')

    else:
        print()
        print('Игрок 2, у вас (O), введите номер ячейки', end=' --> ')