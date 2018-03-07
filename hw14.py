# 14.	Написать функцию, которая будет проверять четность некоторого числа.
# 		def is_even(number): # returns boolean value
# 			pass

def is_even(number):
    if number % 2 == 0:
        result = True
    else:
        result = False
    return result

print('Ваше число четное?', is_even(68))
