# 21.	Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
# def get_max_digit(number): # returns int
# 		     pass

import random
def get_max_digit(big_number):
    print('Случайно сгенерированное 12-тизначное число: ', big_number)
    big_number_str = str(big_number)
    number = '0'
    for num in big_number_str:
        if num > number:
            number = num
    return number

big_number = random.randint(1e11, 1e12-1)
print('Самая большая цифра в числе: ', get_max_digit(big_number))
