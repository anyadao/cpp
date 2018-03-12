# 18.	Каждому символу в таблице символов Unicode соответствует число.
# Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам,
# стоящим между двумя заданными включительно. Например, в функцию передаются символы ‘x’ и ‘z’.
#  Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.
# 		def sum_symbol_codes(first, last): # returns int
# 			pass

def sum_symbol_codes(first, last):
    symbol_first_int = ord(first)
    symbol_last_int = ord(last)
    sum = 0
    for i in range(symbol_first_int, symbol_last_int + 1):
        sum += i
    return sum
symbol_first = input('Введите первый символ: ')
symbol_last = input('Введите второй символ: ')
print(sum_symbol_codes(symbol_first, symbol_last))