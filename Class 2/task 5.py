# Реализуйте алгоритм перемешивания списка.

import random

def input_list(n, input: list):
    for i in range(0, n):
        input.append(random.randint(1, 10))

def shuffle_index(indx: list, len: int):
    i = 0
    while i < len:
        t = random.randint(0, len-1)
        if t not in indx:
            indx.append(t)
            i += 1
        else:
            t = random.randint(0, len)

#
# Изначально я реализовал алгоритм с помощью встроенного функционала
# 

n = int(input("Введите число N --> "))
input = []
input_list(n, input)
print(input)
random.shuffle(input)
print(input)

#
# А затем попытался придумать свой алгоритм. Кажется, получилось
#

n = int(input("Введите число N --> "))
input = []
check = []
result = []
input_list(n, input)
print(input)
shuffle_index(check, len(input))
print([input[x] for x in check])