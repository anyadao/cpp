# 25.	Создайте список на 50 элементов из всех нечётных чисел от 1 до 99 и передайте его в функцию,
#  которая перемешает его элементы в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
# 	Примечание: использовать метод random.shuffle не допускается.
#
#      def shuffle_list(list_to_shuffle): # no return (shuffles list in place)
# 		pass
import random
def shuffle_list(list_to_shuffle):
    list_of_values = []
    start = 0
    for index in range(len(list_to_shuffle) - 1):
        random_index = random.randint(index, len(list_to_shuffle)-1)
        while list_to_shuffle[random_index] in list_of_values:
            random_index = random.randint(start, len(list_to_shuffle) - 1)
        saved_value =  list_to_shuffle[index]
        list_to_shuffle[index] = list_to_shuffle[random_index]
        list_to_shuffle[random_index] = saved_value
        list_of_values.insert(index, list_to_shuffle[random_index])
    return (list_to_shuffle)

odd_list = []
for i in range(100):
    if i % 2 != 0:
        odd_list.append(i)
print(shuffle_list(odd_list))