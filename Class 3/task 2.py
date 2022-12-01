# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def times_pair(source: list, result: list) -> list:
    for i in range(0, (len(source)//2 + len(source) % 2)):
        result.append(source[i] * source[-i-1])
    return result


list_ = [2, 3, 4, 5, 6]
print(times_pair(list_, result=[]))
