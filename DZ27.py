"""Пользователь вводит текст(строка).
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов.
Определите, сколько различных слов содержится в этом тексте.

Input: She sells sea shells on the sea shore
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore
I'm sure that the shells are sea shore shells

Output: 13 (или 15)
"""

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shoreI'm sure that the shells are sea shore shells"
print(len(set(text.upper().split())))
# len - количество элементов, set - уникальные элементы, upper - преобразуем строку в верхний регистр, split - разделяем строку по пробелам