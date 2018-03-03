#ƒана строка с именем студента, в которой им€ предшествует фамилии, например  СMark ZuckerbergС.
# Ќаписать программу, котора€ преобразует эту строку, став€ фамилию на первое место, а им€ на второе.
# “.е. СMark ZuckerbergС -> СZuckerberg MarkС.


fullname = 'Anya Dao'
fullname_components = fullname.split(' ')
fullname_reverse = [fullname_components[1], fullname_components[0]]
space = ' '
print(space.join(fullname_reverse))
