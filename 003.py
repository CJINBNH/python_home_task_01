# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату X '))
y = int(input('Введите координату Y '))

def chetvert(x,y):
    a = 4
    if x > 0 and y > 0:
        a = 1
    elif x < 0 and y > 0:
        a = 2
    elif x < 0 and y < 0:
        a = 3
    print(f"Точка находится в {a} четверти плоскости")

chetvert(x,y)