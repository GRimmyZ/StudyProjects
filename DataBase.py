#%%
import sqlite3 as sl
from pandas import *
from datetime import datetime

with sl.connect(r"C:\Users\Хозяин\Desktop\PythonProjects\SQL\ABD.db"
                ) as db:  #Расположение файла на моем ПК
    cursor = db.cursor()
    query = """SELECT * FROM Instruments"""
    query1 = """SELECT 
                    COUNT(instrumentId)
                FROM Trades
                WHERE instrumentId == 6 and price between 4.9 and 5.0;"""
    query2 = """SELECT 
                    traded
                FROM Trades
                WHERE instrumentId == 6 and price between 4.9 and 5.0;"""
    query3 = """INSERT INTO Instruments (id, className, instrumentName) VALUES (777, 'TQBR', 'LKOH')"""
    #cursor.execute(query3) #Добавление элемента в таблицу Instruments
    dt = []
    for value in cursor.execute(query2):  #Перевод времени из UNIX формата
        dt.append(datetime.utcfromtimestamp(*value).strftime('%H:%M:%S'))
    #Вывод таблиц
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print('База данных содержит следующие таблицы:')
    for table in tables:
        print(*table)
    print('')
    #Вывод записей таблицы Instrument
    print('Таблица "Instrument" содержит следующие данные:')
    for value in cursor.execute(query):
        print(value)
    print('')

    # Таблица "Trades"
    for value in cursor.execute(query1):
        print(
            'В таблице "Trades" с инструкментом "IRAO" сделок в диапазоне 4.9 - 5.0 совершено:',
            *value)
    print('')

    count = 0
    for el in dt:
        if int(el[:2]) < 12:
            count += 1
    print(
        "Совершено сделок с инструкментом IRAO в диапазоне 4.9 - 5.0 в первой половине дня:",
        count)
    db.commit()
# %%
