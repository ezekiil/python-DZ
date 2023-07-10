

# создаем словарь, в котором "ключ" - номер холодильник
string = {"1":"222anton456", "2":"a1n1t1o1n1", "3":"0000a0000n0000t0000o0000n", "4":"gylfole", "5":"richard", "6":"ant0n"}

def Check_Virus(string, virus): # функция проверки
    for i in virus: # цикл проверки всех элементов по буквам вируса
        if i not in string:
            return ("Ok")
        else:
            string = string[string.index(i):] # с помощью среза удалям букву, которую проверили
    return ("Virus")

for i in string: # цикл для печати строки
    print(f'{i}: - {Check_Virus(string[i], "anton")}') # вывод ключа и его значение