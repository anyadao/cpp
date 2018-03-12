# 19.	Написать функцию для поиска разницы между максимальным и минимальным числом среди num_limit
# случайно сгенерированных чисел в указанном числовом диапазоне.
# 		def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
# 			pass
import random
def diff_min_max(num_limit, lower_bound, upper_bound):
    numbers = []
    for i in range(num_limit):
        numbers.append(random.randint(lower_bound, upper_bound))
    max_num = numbers[0]
    min_num = numbers[0]
    for i, elem in enumerate(numbers):
        if max_num < numbers[i]:
            max_num = numbers[i]
        if min_num > numbers[i]:
            min_num = numbers[i]
    return max_num - min_num

print(diff_min_max(10, 0, 26))
