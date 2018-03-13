# 21.	Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
# def get_max_digit(number): # returns int
# 		     pass

import random
def get_max_digit(big_number):
    print('Случайно сгенерированное 12-тизначное число: ', big_number)
    str_big_number = str(big_number)
    number = 0
    big_number = []
    for i in range(12):
        big_number.append(int(str_big_number[i]))
        if big_number[i] > number:
            number = big_number[i]
    return number

big_number = random.randint(100000000000, 999999999999)
print('Самая большая цифра в числе: ', get_max_digit(big_number))