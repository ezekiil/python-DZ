'''Напишите программу для печати всех уникальных значений в словаре. 

Input: [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"},
{"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}] 

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

s = set() # пустой список
d = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}] # словарь

for i in d: # цикл по словарю
    for value in i: # цикл по значениям
        if value not in s: # проверка на уникальность - не находится в списке
            s.add(i[value]) # добавление в список уникальных значений
print(s) # вывод списка