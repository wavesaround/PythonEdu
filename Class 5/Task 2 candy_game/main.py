# # Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import os
import sys
import random

def opening():
    os.system('clear')
    with open(r'text.txt', 'r') as start_message:
        starting = start_message.read()

    print(starting)
    print()
    start_key = input('Введите Y, чтобы начать. N, чтобы остановить игру --> ').lower()
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
        return int(input(f'Игрок {person}, введите целое число --> '))           
    if int(input_num) > max_candies or int(input_num) < 0:                            # range from to verif.
        return int(input(f'Игрок {person}, введите число от 0 до 28 --> '))
    else:                                                                    # return true
        return int(input_num)
        
def set_input(switch: int) -> str:                                           # player choice
    global lottery
    if switch == 1:
        lottery = 2
        return verify((input('Игрок 1 --> ')), switch)
    else:
        lottery = 1
        return verify((input('Игрок 2 --> ')), switch)



####### start game #######

candy_count = 100           # total candies
lottery = lot()             # lottery = start random
temp = 0                    # number of winner
max_candies = 28            # max number of candies

opening()                   # start message and Y/N input

while not candy_count < 0:
    temp = lottery
    candy_count -= set_input(lottery)
print()    
print(f'Игрок {temp} забирает все конфеты')
print()

###########################