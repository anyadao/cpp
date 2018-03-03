#Преобразовать строку с американским форматом даты в европейский. Например, "05.17.2016" преобразуется в "17.05.2016"

american_data = '05.17.2016'
data_components = american_data.split('.')
dot = '.'
european_data = [data_components[1], data_components[0], data_components[2]]
print (dot.join (european_data))
