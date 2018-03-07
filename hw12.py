#12.	Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
#  введенного пользователем в консоли, без использования операторов цикла. a) cо строками,
# б) без использования строк.
#def sum_of_digits(number): # returns int
			#pass

def sum_string(digit):
    one = int(digit[0])
    two = int(digit[1])
    three = int(digit[2])
    return one + two + three

def sum_nostring(digit):
    one = digit // 100
    one_comp = digit % 100
    two = one_comp // 10
    three = one_comp % 10
    return one + two + three

print(sum_nostring(356))
print(sum_string('356'))