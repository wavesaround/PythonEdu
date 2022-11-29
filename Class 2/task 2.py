# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

n = int(input("Введите число N --> "))
i = 1

while i <= n:
    times = 1
    for x in range(1, i+1):
        times *= x
    i += 1
    print(times, end=" ")
