# 15.	Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
#  Каждая окружность задается координатами центра и радиусом.
# def cirles_intersects(x1, y1, r1, x2, y2, r2): # returns boolean value
# 			pass

import math
def circles_intersects(x1, y1, r1, x2, y2, r2):
    if r1 > r2:
        radius_sum = r1 + r2
        radius_difference = r1 - r2
        distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow((y1 - y2), 2))
        if distance == radius_sum or distance == radius_difference or (distance < radius_sum and distance > radius_difference):
            answer = True
        if distance > radius_sum or distance < radius_difference:
            answer = False
        return answer

    if r1 < r2:
        radius_sum = r1 + r2
        radius_difference = r2 - r1
        distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow((y2 - y1), 2))
        if distance == radius_sum or distance == radius_difference or (distance < radius_sum and distance > radius_difference):
            answer = True
        if distance > radius_sum or distance < radius_difference:
            answer = False
        return answer
    if r1 == r2:
        radius_sum = r1 + r2
        distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow((y2 - y1), 2))
        if distance == radius_sum or distance == 0 or (distance < radius_sum and distance > 0):
            answer = True
        if distance > radius_sum or distance < 0:
            answer = False
        return answer


print(circles_intersects(0, 0, 4, 0, 0, 4))
print(circles_intersects(0, 0, 5, 0, 0, 4))
print(circles_intersects(0, 0, 4, 0, 0, 5))


