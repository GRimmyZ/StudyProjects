#%%
from random import *


def generate_password(q1, q2, chars):  #Длина, строка символов
    password = ''
    for _ in range(int(q1)):
        for el in range(int(q2)):
            el = choice(chars)
            password = password + el
        password = password + '   '
    return password


#Константы учавствующие в генерации пароля
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
chars = ''
q1 = input('Введите количество паролей для генерации')
q2 = input('Введите длину пароля')
q3 = input('Включать ли цифры в пароль ( + / - )')
q4 = input('Включать ли прописные буквы ( + / - )')
q5 = input('Включать ли строчные буквы ( + / - )')
q6 = input('Включать ли символы ( + / - )')
q7 = input('Исключать ли неоднозначные символы (iIl1LoO0)( + / - )')
if q3 == '+':
    chars = chars + digits
if q4 == '+':
    chars = chars + lowercase_letters
if q5 == '+':
    chars = chars + uppercase_letters
if q6 == '+':
    chars = chars + punctuation
if q7 == '+':
    for _ in chars:
        for el in 'iIl1LoO0':
            if _ == el:
                ind = chars.index(_)
                chars = chars[:ind] + chars[ind + 1:]
print('Ваш новый пароль:', generate_password(q1, q2, chars))
# %%
