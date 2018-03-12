# 23.	Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.
# Пользователь вводит число, а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше.
#  После чего опять просит угадать. И так пока пользователь не угадает выбранное число.

import random
def guess_game():
    number = 0
    computer_number = random.randint(1, 10)
    while number != computer_number:
        number = int(input('Введите цифру: '))
        if number < computer_number:
            print('Число больше!!!')
        if number > computer_number:
            print('Число меньше!!!')
    return print('Ура! Вы угадали!')

guess_game()