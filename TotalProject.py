#%%
import sqlite3 as sl
from pandas import *
from datetime import datetime
import matplotlib as mpl

with sl.connect(
        r"C:\Users\Хозяин\Desktop\PythonProjects\TotalProjectfordiplom\ABD-VKR.db"
) as db:  #Расположение файла на моем ПК
    cursor = db.cursor()  #Курсор движущийся в БД
    query1 = """SELECT 
                    instrumentName,
                    className
                FROM Instruments
                ORDER BY className;
             """ #Запрос на группировку Инструментов по классам
    query2 = """SELECT 
                    traded
                FROM Trades
                WHERE instrumentId == 6 and price between 4.9 and 5.0;""" #Запрос для оценки времени
    query3 = """SELECT 
                    instrumentId,
                    price,
                    nQty
                FROM Trades;""" #Запрос на вывод сделок
    query4 = """SELECT
                    id,
                    instrumentName    
                FROM Instruments;"""# Запрос на соединение id Инструмента и его тикера
    query5 = """SELECT
                    instrumentId,
                    price,
                    nQty    
                FROM Trades
                WHERE instrumentId == ident;"""# Запрос id Инструмента и операций с ним
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    #print('База данных содержит следующие таблицы:') #Вывод названий таблиц из БД
    #for table in tables:
    #    print(*table)
    dt = []
    for value in cursor.execute(query2):  #Перевод времени из UNIX формата
        dt.append(datetime.utcfromtimestamp(*value).strftime('%H:%M:%S'))
    #
    groupInstrum = dict()  #Словарь сгруппированных инструментов
    for el in cursor.execute(query1):
        if el[1] not in groupInstrum.keys():
            groupInstrum[el[1]] = [(el[0])]
        else:
            groupInstrum[el[1]].append(el[0])
    instId = {}
    for istrumentID in cursor.execute(query4):
        if istrumentID[1] not in instId.keys():
            instId[istrumentID[1]] = (istrumentID[0])
    if input(
            'Вы хотите проверить как сгруппированы инструменты? (Да/Нет)') in {
                'Да', 'да', 'lf', 'Lf', 'LF', 'ДА'
            }:
        for k in groupInstrum.keys():
            print('В классе', k, 'содержатся следующие тикеры инструментов:',
                  *groupInstrum[k])
    #
    tiker = input(
        'Выберите класс инструментов, о котором хотите получить информацию:'
    ).upper()
    if tiker in groupInstrum.keys():
        if tiker == 'TQBR':
            print('Вы выбрали класс акций.',
                  'Выберите тикер интересующего вас инструмента:',
                  *groupInstrum[tiker],
                  sep='\n')
            tikerI = input().upper()
            if tikerI in groupInstrum[tiker]:
                ident = instId[tikerI]

        elif tiker == 'SPBFUT':
            print('Вы выбрали класс фьючерсов.',
                  'Выберите тикер интересующего вас инструмента:',
                  *groupInstrum[tiker],
                  sep='\n')
            tikerI = input().upper()
            if tikerI in groupInstrum[tiker]:
                ident = instId[tikerI]

        elif tiker == 'SPBXM':
            print('Вы выбрали класс акций иностранных компаний.',
                  'Выберите тикер интересующего вас инструмента:',
                  *groupInstrum[tiker],
                  sep='\n')
            tikerI = input().upper()
            if tikerI in groupInstrum[tiker]:
                ident = instId[tikerI]
    print(ident)
    for value in cursor.execute(query5):
        print(value)
    #for v in cursor.execute(query3):
    #   print(v)
    #db.commit()
# %%
