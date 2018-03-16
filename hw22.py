# 22.	Для удобства проведения вступительных экзаменов всеx абитуриентов в MIT разбивают на группы в зависимости от
# первых букв их фамилии. Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’. Название группы определяет в какую группу
# попадает абитуриент, в зависимости от первой буквы его/ее фамилии. Например, Will Smith попадает в группу ‘Q-T’, т.к.
# первая буква его фамилии попадает в диапазон букв от ‘Q‘ до ‘Т‘ (включительно!).
# Абитуриент Jay Z попадает в группу ‘U-Z’ и т.д. Написать функцию, которая получает список имен студентов вида ['Name1
# Surname1', 'Name2 Surname2', 'Name3 Surname3', ...] и возвращает количество абитуриентов в группах, сформированных по
# их фамилиям, описанным выше образом.
#      def group_by_surname(list_of_enrollees): # returns 4 ints
# 			pass

import re
def group_by_surname(list_of_enrolles):
    group1 = 0
    group2 = 0
    group3 = 0
    group4 = 0
    length = (len(list_of_enrolles))
    for i in range(length):
        name_parts = list_of_enrolles[i].split(' ')
        surname = name_parts[1]
        letter = surname[0]
        if re.match('[a-iA-I]', letter):
            group1 += 1
        elif re.match('[j-pJ-P]', letter):
            group2 += 1
        elif re.match('[q-tQ-T]', letter):
            group3 += 1
        elif re.match('[u-zU-Z]', letter):
            group4 += 1
    return group1, group2, group3, group4

list_of_enrolles = ['John Aearson','Ruth Shelton','Silvia Bryan','David Flaming','Harry Bates']
print(group_by_surname(list_of_enrolles))

