# 30.	Написать функцию, возвращающую все простые числа от 1 до 100.
#
# def gen_primes(): # returns list of ints
# 			pass

def gen_primes():
    simple_list = []
    len = 100
    start = 2
    for number in range(start, len+1):
        for check in range(start, number):
            if number % check == 0:
                break
        else:
            simple_list.append(number)
    return simple_list

print(gen_primes())