# 16.	Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути.
# Через 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.
# def have_trains_crashed(v1, v2): # returns boolean value
# 			pass

def have_trains_crashed(v1, v2):
    distance1 = 4
    time1 = v1 / distance1
    distance2 = 6
    time2 = v2 / distance2
    if time1 > time2:
        return False
    if time2 > time1:
        return True
    if time1 == time2:
        return True

print('Столкнутся поезда?', have_trains_crashed(4, 6))
print('Столкнутся поезда?', have_trains_crashed(8, 79))
