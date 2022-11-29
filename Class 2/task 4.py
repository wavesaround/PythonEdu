# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел

n = int(input("Введите число N --> "))
search_string = input("Введите индексы через пробел ---> ").split()
result = 1

range = range(-n, n+1)
list = list(range)

for x in search_string:
    result *= list[int(x)]

print(result)