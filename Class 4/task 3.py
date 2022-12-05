# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

def input_list(lengths: int) -> list:
    new_l = []
    for x in range(0, lengths):
        new_l.append(random.randint(1, lengths))      
    return new_l

def unicum(first: list) -> list:
    res = []
    for x in first:
        if first.count(x) == 1:
            res.append(x)
    return res        

n = 8
input_l = input_list(n)
print(f'Ввод -> {input_l}')
print(f'Вывод -> {unicum(input_l)}')
