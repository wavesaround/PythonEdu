# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

n = int((input("Введите число --> ")).replace('.', '').replace(',', ''))
sum = 0

while n > 0:
    sum += (n % 10)
    n //= 10

print(sum)