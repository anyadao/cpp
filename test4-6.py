# 4. Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры
# 5. Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем.
# Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.
# 6. Определить является ли строка изограммой (https://en.wikipedia.org/wiki/Isogram ), т.е. что все буквы в
#  ней за исключением пробелов встречаются только один раз. Например, строки 'Питон', 'downstream', 'книга без слов'
# являются изограммами, а само слово 'изограмма' - нет.

#__________________________________________TASK_NUMBER_4____________________________________________
def odd_multiply(number):
    multiply_odd = 1
    odd_list = [int(digit) for digit in number if int(digit) % 2 != 0]
    for digit in odd_list:
        multiply_odd *= digit
    return multiply_odd

number = input('Введите пятизначное число: ')
if len(number) == 5:
    print('Произведение нечетных цифр в вашем числе: ', odd_multiply(number))
else:
    print('Вы ввели неверные данные')

#___________________________________________TASK_NUMBER_5______________________________________________
def coordintaion(element):
    coord = 10
    return abs(coord - element)

def near_to_ten(input_list):
    input_list.sort(key=coordintaion)
    print('Ваш отсортированный список координат приближенных к 10:', input_list)
    return input_list

def input_list():
    pois = input('Введите список элементов для сравнение близости координат через пробел: ')
    pois_list = [int(digit) for digit in pois.split(' ')]
    print('Ваш список: ', pois_list)
    return pois_list

near_to_ten(input_list())

#________________________________________TASK_NUMBER_6____________________________________________

def input_text():
    text = input('Введите текст или слово для определения изограмма это или нет: ')
    return text


def izogram(input_text):
    space = ' '
    start = 0
    for char in input_text:
        start += 1
        if space in char:
            continue
        if char in input_text[start:]:
            print('Ваше слово или текст не является изограммой')
            return False
    else:
            print('Ваше слово или текст является изограммой.')
            return True

print(izogram(input_text()))