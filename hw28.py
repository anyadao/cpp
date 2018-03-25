# 28.	Создать программу, которая запрашивает у пользователя произвольную строку символов.
#  Далее программа ее шифрует и выводит на экран в зашифрованном виде. Шифрование происходит путем замены каждого
# символа символом, который находится на 5 позиций правее в предопределенной таблице шифрования.
# Таблица шифрования задается программистом в виде одномерного списка символов латинского алфавита от a до z.
# Если при выборе символа для шифровки таблица шифрования заканчивается, то циклически переходить к ее началу.
# Отсутствующие в таблице шифрования символы, записываются в результирующую строку без изменений. Регистр игнорируется.
# 	Таблица шифрования (a,b,c,d,...,x,y,z,0,1,2,3,4,5,6,7,8,9)
# 	Например: Исходная строка, которую ввел пользователь: 'secret', 'Office 365'
# 	Зашифрованная строка, которую выдала программа: 'xjhwjy', 'tkknhj 8ba'
# 	Примечание: т.н. таблица шифрования может быть представлена как строка или список.
#
# def encode(str_to_encode): # returns enсoded string
# 		pass
import re
import string

def encode(str_to_encode):
    encrypted = ''
    shift = 5
    #encryption_table = 'abcdefghijklmnopqrstuvwxyz0123456789'
    encryption_table = str(string.ascii_lowercase + string.digits)
    parts = str_to_encode.split(' ')
    length_of_table = len(encryption_table)
    length_parts = len(parts)
    for word in parts:
        length_word = len(word)
        for i in range(len(word)):
            for j in range(length_of_table):
                if word[i] == encryption_table[j]:
                    if(j + shift) < length_of_table:
                        encrypted += encryption_table[j + shift]
                    else:
                        difference = (j + shift) - length_of_table
                        encrypted += encryption_table[difference]
                        continue
        if re.search('[.,:!?-]', word):
            encrypted = encrypted + word[length_word-1]
        if length_parts > 1:
                encrypted += ' '
                length_parts -= 1
    return encrypted

info = input('Напишите строку, которую необходимо зашифровать: ')
print(encode(info))
