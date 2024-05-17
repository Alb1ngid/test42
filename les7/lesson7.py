# sql - язык структурированных запросов

# модули библиотеки

# субд - система управления базами данных
# relation norelation

# бд - база данных:

# CRUD - create read update delete
import sqlite3

# connect-создает или подключается к базе данных
db = sqlite3.connect('42.db')

# cursor-щбращается к командам sql
cur = db.cursor()

# cur.execute('''DROP TABLE IF EXISTS пользователи''')
# drop-удалает таблицу

#сreate - создает таблицу
# if not exists - не вызывает ошибку если такая таблица уже есть
#
cur.execute('''CREATE TABLE IF NOT EXISTS клиенты(
имя TEXT,
возраст INTEGER,
дата DATE,
хобби TEXT
)''')

# execute- для того чтобы писать язык sql в других файлах
# CREATE
# INSERT -добавит или закрепить
#  into - выбрать

# cur.execute('''INSERT INTO клиенты
# (имя,возраст,хобби) VALUES
# ('beka',20,''),
# ('bekbolot',21,''),
# ('alibek',15,'')
# ''')


#update-update
# set - функция изменения поля
cur.execute('''UPDATE клиенты 
SET дата="2003-06-06"
WHERE rowid=1
''')

cur.execute('''UPDATE клиенты 
SET хобби='ничего'
where имя='beka'
''')

# delete -delete
cur.execute('''DELETE FROM клиенты 
WHERE rowid>5''')

# read
# SELECT- похож на return
cur.execute('''SELECT rowid,* FROM клиенты''')

# fetchhall-аналог print()
for i in cur.fetchall():
    print(i)

# commit-сохраняет результат
db.commit()
#close - закрывает базу данных
db.close()





