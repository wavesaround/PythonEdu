# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def sum(numbers: list):
    res = 0
    for i in range(1, len(numbers) - 1, 2):
        res += numbers[i]
    return res


list_ = [2, 3, 5, 9, 3, 5, 7, 3, 2]
print(sum(list_))
