# 13.	Пользователь вводит длины катетов прямоугольного треугольника.
# Написать функцию, которая вычислит площадь треугольника и его периметр.
# Результат работы функции должен вернуть два значения.
# def triangle_square_and_perimeter(a, b): # returns 2 values
# 			pass

import math
def triangle_square_and_perimeter(katheter1, katheter2):
    square = (katheter1 * katheter2) / 2
    perimetr = math.hypot(katheter1, katheter2) + katheter1 + katheter2
    return square, perimetr


square, perimetr = triangle_square_and_perimeter(10, 12)
print('Площадь прямоугольного треугольника равна: %d см, а периметр прямоугольного треугольника равен: %d см'
      %(square, perimetr))