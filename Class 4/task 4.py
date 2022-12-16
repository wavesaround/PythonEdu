# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x^4) + 9*(x^3) + 1*(x^2) + 5*x + 4 = 0 или 8*(x^4) + 5*x + 4 = 0 и т.д.

import random

def rand():
    return random.randint(0, 10)

def model(k: int, rand: int):
    if rand == 0:
        pass
    elif k == 0:
        print(f'{rand}', end=' ')
    elif k == 1:
        print(f'{rand}x', end= ' + ')
    else:
        print(f'{rand}(x^{k})', end= ' + ')

def controller(k: int):
    while not k < 0:
        model(k, rand())
        k -= 1
    print('= 0')

k = 4
controller(k)