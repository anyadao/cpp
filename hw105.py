# 102.	Implement the below function:
#
# def is_valid_credit_card(credit_card):
#     """
#     Given a value determine whether or not it is valid per the Luhn formula.
#     The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers,
# such as credit card numbers.
#     The task is to check if a given string is valid.
#     Strings of length 1 or less are not valid.
#  Spaces are allowed in the input, but they should be stripped before checking.
#  All other non-digit characters are disallowed.
#
#     Example 1: valid credit card number
#
#         4539 1488 0343 6467
#
#         Step 1
#         The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling
#         4_3_ 1_8_ 0_4_ 6_6_
#
#         Step 2
#         If doubling the number results in a number greater than 9 then subtract 9 from the product.
#         The results of our doubling:
#         8569 2478 0383 3437
#
#         Step 3
#         Then sum all of the digits:
#         8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
#
#         Step 4
#         If the sum is evenly divisible by 10, then the number is valid. This number is valid!
#
#     Example 2: invalid credit card number
#
#         8273 1232 7352 0569
#
#         Step 1, 2
#         Double the second digits, starting from the right
#         7253 2262 5312 0539
#
#         Step 3
#         Sum the digits
#         7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57
#
#         Step 4
#         57 is not evenly divisible by 10, so this number is not valid.
#
#     :param score: credit card to check (string)
#     :return: True if valid, False otherwise
#     """
#     pass

import re
def is_valid_credit_card(credit_card):
    cre_card_comp = re.findall(r'\d', credit_card)
    print('Номер вашей кредитной карты:', credit_card)
    sum = 0
    
    for i, elem in enumerate(cre_card_comp):
        cre_card_comp[i] = int(elem)

    for i, elem in enumerate(cre_card_comp):
        if i % 2 == 0:
            cre_card_comp[i] = elem * 2
            if cre_card_comp[i] > 9:
                cre_card_comp[i] -= 9
        sum += cre_card_comp[i]

    if sum % 10 == 0:
        return True
    else:
        return False

print(is_valid_credit_card('4539 1488 0343 6467'))