#Ќаписать программу, котора€ преобразует им€ переменной в формате snake_case в формат CamelCase.
#  ƒл€ простоты считаем, что им€ переменной всегда состоит из 3-х слов. Ќапример: Сemployee_first_nameТ -> 
# СEmployeeFirstNameТ

snake_case_phrase = 'employee_first_name'
phrase_components = snake_case_phrase.split('_')
str = [phrase_components[0].capitalize(), phrase_components[1].capitalize(), phrase_components[2].capitalize()]
nospace = ''
print(nospace.join(str))

