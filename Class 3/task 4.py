# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = 123
c = ''

while a > 0:
    c += f'{a % 2}'
    a //= 2

print(c[::-1])