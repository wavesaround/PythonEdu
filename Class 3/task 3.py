# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

def search(numbers: list) -> float:
    max = numbers[0] % 1
    min = numbers[0] % 1
    for i in numbers:
        if i % 1 > max:
            max = i % 1
        if i % 1 < min:
            min = i % 1
    return round(max - min, 2)


list_ = [1.1, 1.2, 3.1, 10.01]
print(search(list_))
