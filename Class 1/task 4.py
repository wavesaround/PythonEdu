# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)

number = float(input("Введите номер четверти --> "))

if number < 1 or number > 4:
    print("Введите значение от 1 до 4")

elif number == 1:
    print("x > 0 ; y > 0")

elif number == 2:
    print("x < 0 ; y > 0")

elif number == 3:
    print("x < 0 ; y < 0")

elif number == 4:
    print("x > 0 ; y < 0")