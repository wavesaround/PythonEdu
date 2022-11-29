ax = float(input("Введите координаты оси x --> ").replace(',', '.'))
ay = float(input("Введите координаты оси y --> ").replace(',', '.'))
bx = float(input("Введите координаты оси x --> ").replace(',', '.'))
by = float(input("Введите координаты оси y --> ").replace(',', '.'))

dest = ((bx - ax)**2 + (by -ay)**2)**(0.5)
print(round(dest, 2))