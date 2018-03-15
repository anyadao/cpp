# 26.	Создайте список из 11 случайных целых чисел из отрезка [-1;1].
# Передайте его в функцию, которая определит какой элемент встречается в списке чаще всего и вернет этот элемент.
#  Однако, если два каких-то элемента встречаются одинаковое количество раз, то вернуть None, а не самый часто
# встречающийся элемент.
#      def calc_frequency(lst): # returns the most frequent number or None
# 		pass

import random
def calc_frequency(list):
    minus1 = 0
    zero = 0
    one = 0
    for i, elem in enumerate(list):
        if elem == -1:
            minus1 += 1
        elif elem == 0:
            zero += 1
        elif elem == 1:
            one +=1
    if minus1 == zero or zero == one or minus1 == one:
        return None
    else:
        maximum = max(minus1, zero, one)
        if maximum == minus1:
            return -1
        if maximum == zero:
            return 0
        if maximum == one:
            return 1

list = []
for i in range(11):
    list.insert(i, random.randint(-1, 1))
print(calc_frequency(list))