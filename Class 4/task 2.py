# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in_list = tuple([x for x in range(2,10)])
# print(in_list)


def search_multis(x: int, dict: tuple):
    i = 0
    item = dict[i]
    while x != 1:
        if x % item == 0:
            print(item, end=' ')
            x //= item
        elif i == len(dict) - 1:
            item = x
        else: 
            i+=1
            item = dict[i]

n = int(input('Введите число n --> '))
dict_ = (2, 3, 5, 7, 11, 13, 17, 19, 23)
search_multis(n, dict_)