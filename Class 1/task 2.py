# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("input x --> "))
y = int(input("input y --> "))
z = int(input("input z --> "))

left = not(x or y or z)
right = not x and not y and not z

if  left == right:
    print("True")
else:
    print("False")