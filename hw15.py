# 15.	Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
#  Каждая окружность задается координатами центра и радиусом.
# def cirles_intersects(x1, y1, r1, x2, y2, r2): # returns boolean value
# 			pass

import math
def circles_intersects(x1, y1, r1, x2, y2, r2):
    min_radius = min(r1, r2)
    max_radius = max(r1, r2)
    radius_sum = r1 + r2
    radius_difference = max_radius - min_radius
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow((y1 - y2), 2))
    if distance == radius_sum or distance == radius_difference or (distance < radius_sum and distance > radius_difference):
        return True
    if distance > radius_sum or distance < radius_difference:
        return False

print(circles_intersects(0, 0, 4, 0, 0, 4))
print(circles_intersects(0, 0, 5, 0, 0, 4))
print(circles_intersects(0, 0, 4, 0, 0, 5))


