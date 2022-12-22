import os
import sys
import random
import bot_brain

def opening():
    os.system('clear')
    with open(r'text_bot.txt', 'r') as start_message:
        starting = start_message.read()
    print(starting)
    print()
    start_key = input(
        'Введите Y, чтобы начать. N, чтобы остановить игру --> ').lower()
    if start_key == 'y':
        pass
    else:
        sys.exit('-- Игра завершена --')


def lot() -> int:                                                            # random from 1 to 2
    x = random.randint(1, 100)
    if x > 50:
        return 1
    else:
        return 2


def verify(input_num: int, person: int):
    global max_candies
    if input_num.isdigit() == False:                                         # int verification
        return int(input(f'Игрок, введите целое число --> '))
    if int(input_num) > max_candies or int(input_num) < 0:                   # check max candies
        return int(input(f'Игрок, введите число от 0 до 28 --> '))
    else:                                                                    # return true
        return int(input_num)


def win(temp: int):
    if temp == 1:
        return 'Человек забирает все конфеты'
    else:
        return 'Бот забирает все конфеты'


def set_input(switch: int) -> str:                                           # player choice
    global lottery, memory_bot, max_candies
    if switch == 1:
        lottery = 2
        return verify((input('Человек --> ')), switch)
    else:
        lottery = 1
        t = bot_brain.go(memory_bot, max_candies)
        print(f'    Бот --> {t}')
        return t

####### start bot game #######


def start():
    global candy_count, lottery, temp, max_candies, memory_bot
    opening()                        # <-- start message
    while not candy_count < 0:
        temp = lottery
        result = set_input(lottery)
        candy_count -= result
        if lottery == 2:
            memory_bot = result
    print()
    print(win(temp))
    print()

######## settings ########


candy_count = 2021          # total candies
lottery = lot()             # lottery = start random
temp = 0                    # number of winner
max_candies = 28            # max number of candies
memory_bot = 0