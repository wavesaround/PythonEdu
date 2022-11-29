# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму

n = int(input("Введите число N --> "))
result = 0

for x in range(1, n+1):
    result += (1 + 1 / x)**x
print(round(result, 2))