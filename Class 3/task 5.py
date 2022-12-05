# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

def Fibonachi(k: int) -> list:
    results = [0, 1]
    count = 2
    while count <= k:
        results.append(results[count-2] + results[count-1])
        count += 1
    return results

def negaFibonachi(k: int) -> list:
    results = [1, -1]
    count = 2
    while count <= k-1:
        results.append(results[count-2] - results[count-1])
        count += 1
    return results

k = int(input('Введите значение k --> '))
new_list = negaFibonachi(k)
new_list.reverse()
new_list += Fibonachi(k)
print(new_list)