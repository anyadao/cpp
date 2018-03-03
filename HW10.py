#Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase.
# Для простоты считаем, что имя переменной всегда состоит из 3-х слов. Например: ‘employee_first_name’ ->
# ‘EmployeeFirstName’

snake_case_phrase = 'employee_first_name'
phrase_components = snake_case_phrase.split('_')
str = [phrase_components[0].capitalize(), phrase_components[1].capitalize(), phrase_components[2].capitalize()]
nospace = ''
print(nospace.join(str))

