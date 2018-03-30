#1. (a + b * c)2  2. a - 4 * b / c  3. (a * b + 4) / (c - 1)

def first_expression(a, b, c):
    return print('Result1: ', (a + b * c)**2)

def second_expression(a, b, c):
    return print('Result2: ', a - (4 * b) / c)

def third_expression(a, b, c):
    return print('Result3: ', (a * b + 4) / (c - 1))

print('Введите данные a, b, c с клавиатуры через enter! ')
a = int(input())
b = int(input())
c = int(input())

first_expression(a, b, c)
second_expression(a, b, c)
third_expression(a, b, c)

