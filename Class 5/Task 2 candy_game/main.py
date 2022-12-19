import p2p
import bot

def st_choice():
    print('Выбери режим игры')
    print()
    temp = int(input('1 - мультиплеер, 2 - бот : '))
    if temp == 1:
        return p2p.start()
    if temp == 2: 
        return bot.start()

st_choice()