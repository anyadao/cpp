# 17.	Написать функцию решения квадратного уравнения.
# 		def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots or 2 Nones
# 			pass

import math
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    discriminant_root = math.sqrt(discriminant)
    if a != 0:
        if discriminant < 0:
            return None, None
        elif discriminant == 0:
            root = -b / 2 * a
            return root, None
        elif discriminant > 0:
            root1 = (-b + discriminant_root) / (2 * a)
            root2 = (-b - discriminant_root) / (2 * a)
            return root1, root2

print(solve_quadratic_equation(10, 2, 0))