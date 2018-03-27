# 29.	Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
# -	Пароль состоит из 8 символов
# -	В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
# -	Пароль обязательно должен содержать Большие и маленькие буквы и цифры
#
# def gen_password(): # returns string
# 			pass

import random
import string
import re

def gen_password():
    pass_length = 8
    first_part = 2
    second_part = 5
    third_part = 7
    password = []
    accepted_symbols = list(string.ascii_letters + string.ascii_lowercase + string.digits + chr(95))
    for i in range(pass_length):
        password += str(random.choice(accepted_symbols))
    if not re.search('[0-9]', str(password)):
        password[random.randint(0, first_part)] = random.choice(string.digits)
    if not re.search('[A-Z]', str(password)):
        password[random.randint(first_part, second_part)] = random.choice(string.ascii_uppercase)
    if not re.search('[a-z]', str(password)):
        password[random.randint(second_part, third_part)] = random.choice(string.ascii_lowercase)
    str(password)
    joined_password = ''.join(password)
    return joined_password

print(gen_password())