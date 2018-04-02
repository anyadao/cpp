#7.Найти сумму десяти первых чисел ряда Фибоначчи
# 8. В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.
# 9. Нормировать одномерный список случайных чисел. Нормирование означает приведение всех значений массива к интервалу
#  [-1;1], причем максимальное абсолютное значение элементов после нормирование должно быть равно 1.
# Например, последовательность [-5, 3, 4] после нормирование будет выглядеть [-1, 0.6, 0.8]

#____________________________________________________TASK_NUMBER_7_______________________________________________________
def fibonacci(n):
    if n > 2:
        return (fibonacci(n-1) + fibonacci(n-2))
    elif n == 0:
        return 0
    else:
        return 1

def fibonacci_sum(n):
    fibonacci_list = [fibonacci(i) for i in range(1, n+1)]
    sum_fibonacci = sum(fibonacci_list)
    print('Список чисел Фибоначчи, которые необходимо просуммировать: ', fibonacci_list)
    print('Сумма чисел Фибоначчи: ', sum_fibonacci)

fibonacci_sum(10)

#____________________________________________________TASK_NUMBER_8______________________________________________________

def input_list():
    pois = input('Введите список элементов : ')
    pois_list = [int(digit) for digit in pois.split(' ')]
    print('Ваш список: ', pois_list)
    return pois_list

def min_max_replace(input_list):
    max, min = input_list[0], input_list[0]
    max_index, min_index = 0, 0
    for i in range(len(input_list)):
        if input_list[i] > max:
            max = input_list[i]
            max_index = i
        elif input_list[i] < min:
            min = input_list[i]
            min_index = i
    input_list[min_index], input_list[max_index] = input_list[max_index], input_list[min_index]
    return input_list

print('Ваш список после смены минимально и максимального значения: ', min_max_replace(input_list()))

#_______________________________________________TASK_NUMBER_9____________________________________________

def ration_list(input_list):
    max_number = max([abs(number) for number in input_list])
    raioned_list = [(digit/max_number) for digit in input_list]
    return raioned_list

print(ration_list(input_list()))