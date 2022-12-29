from os import system
from sys import exit
from lottery import lot
import valid, print_, writelist, checkwin
with open(r'info.txt', 'r') as info:
    start_text = info.read()

system('clear')

#####

mainlist = list(range(1, 10))                           # generate list for a game board
flag_bot = 0                                            # index of a game mode
user_switch = 0                                         # user switch
turn_switch = lambda x: 1 if x == 2 else 2              # function of a switch turn between users
win = False                                             # win status

#####

print(start_text)                                       # print start text from file
flag_bot = valid.init(1)                                # input and verification entered value
user_switch = lot()                                     # lottery between users
print()
print('-- Игра началась --')
print()
while win == False:                                     # wait for a win
    print_.board(mainlist)                              # print game board
    print_.go(user_switch)                              # print message for a current user
    writelist.init(mainlist, user_switch)               # write input value to the list
    win = checkwin.init(mainlist, user_switch)          # verif. win
    if win == False:
        user_switch = turn_switch(user_switch)          # if false -> turn to other user
print_.board(mainlist)                                  # if true -> print final board
print(f'Выиграл игрок с номером {user_switch}')         # ...and print the results
exit('-- Игра завершена --')