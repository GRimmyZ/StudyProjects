# %%
from random import *

print('Привет, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут?')
print('Привет', name)
answers = [
    'Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
    'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего	',
    'Хорошие перспективы', 'Звезды говорят - да', 'Да',
    'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать',
    'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
    'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
    'Перспективы не очень хорошие', 'Весьма сомнительно'
]

while True:
    print('Вы встряхнули шар и ваш вопрос?')
    question = input('Задайте вопрос')
    print('Ваш вопрос:', question)
    print(choice(answers))
    reload = input('Вы хотите задать еще вопрос? (Да/Нет)').lower()
    if reload == 'да' or reload == 'lf':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
# %%
