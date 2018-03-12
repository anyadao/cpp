# Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди 100 случайно сгенерированных чисел
# в произвольном числовом диапазоне. Т.е. от суммы четных чисел вычесть сумму нечетных чисел.
# 		def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int

import random
def diff_even_odd(num_limit, lower_bound, upper_bound):
    sum_odd = 0
    sum_even = 0
    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)

        if number % 2 == 0:
            sum_even += number
        elif number % 2 != 0:
            sum_odd += number
    sum_max = max(sum_odd, sum_even)
    sum_min = min(sum_odd, sum_even)
    return sum_max - sum_min

print(diff_even_odd(100, 0, 100))