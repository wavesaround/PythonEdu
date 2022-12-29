def onetwo(number: str) -> int:
    while not number.isdigit():
        number = input('Пожалуйста, введите ЧИСЛО 1 или 2 --> ')
    number = int(number)
    while number < 1 or number > 2:
        number = int(input('Пожалуйста, введите число 1 или 2 --> '))
    return number

def board_write(number: str):
    while not number.isdigit():
        number = input('Пожалуйста, введите ЧИСЛО от 1 до 9 --> ')
    number = int(number)
    while number < 1 or number > 9:
        number = int(input('Пожалуйста, введите число от 1 до 9 --> '))
    return number

def init(mode: int):
    if mode == 1:
        numbers = input('Введите число от 1 до 2 --> ')
        return onetwo(numbers)
    if mode == 2:
        user_num = input()
        return board_write(user_num)