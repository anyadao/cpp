# Написать функцию, которая будет переводить градусы в радианы. Используя эту функцию вывести на
# экран значения косинусов углов в 60, 45 и 40 градусов.
# def degrees2radians(degrees): # returns float 1 градус примерно = 0,0174 радиан
# 			pass

import math
def degrees2radians (degrees):
            radians = math.pi / 180 * degrees
            return radians
print('Перевод градусов в радианы равен: ', degrees2radians(90))

