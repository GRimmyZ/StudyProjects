# %%
from math import *
from random import *
from os import *
from tkinter import *

def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100:
        return True
    else:
        return False


def game():
    print('Добро пожаловать в числовую угадайку!')
    gran_n = int(
        input(
            'Введите большую границу для интервала угадайки (меньшая равна 1)'))
    random_num = randint(1, gran_n)  # Генерация случайного числа
    count = 0
    while True:
        nn = input('Введите число от 1 до ' + str(gran_n) + ' ')
        count += 1
        if is_valid(nn) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        n = int(nn)
        if n < random_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif n > random_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
    print('Вы использовали', count, 'попыток, чтобы угадать число', random_num)
    print('Но его можно было бы найти за', ceil(log2(n)), 'попыток')


game()

while True:
    quest = input(('Поиграем еще? (Да / Нет)'))
    if quest.lower() == 'да' or quest.lower() == 'lf':
        game()
    else:
        print('Нам было весело с тобой, Спасибо!')
        shutdown_command = "shutdown /s /t 00"  #Выключение ПК
        system(shutdown_command)
        break

# %%
