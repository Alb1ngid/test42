# sql - язык для базы данных
# СУБД - система управления базами данных  реояционные и нереляционные
import sqlite3 as sq
# crud - create read update delete

# p=[1,3,42,3,3]
# print(p[2])
with sq.connect('saper.db') as con:
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL,
    pol INTEGER DEFAULT 3,
    old INTEGER DEFAULT 1,
    score INTEGER DEFAULT 0
)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS game(
    id INTEGER,
    nikname TEXT
    )''')
    cur.execute('''INSERT INTO game VALUES (7,'beka')''')
    # cur.execute('''INSERT INTO users(name, pol,score)
    # VALUES ('beka',2,40),('abai',2,40)''')

    #update
    # cur.execute('''UPDATE users SET score=score-5000 WHERE score>10000 ''')

    cur.execute('''DELETE FROM users WHERE score<1''')

    # read
    cur.execute('''SELECT * FROM users ORDER BY score DESC''')
    item=cur.fetchall()
    for i in item:
        print(i)
    print('------------------')
    cur.execute('''SELECT * FROM game''')

    for i in cur.fetchall():
        print(i)
    print('0------------------------------------0')

    cur.execute('''SELECT users.id, game.nikname,users.name,users.score
    FROM users 
    JOIN game on users.id = game.id
    ''')
    for i in cur.fetchall():
        print(i)


    # try:
    #     print('l')
    # Exception = cur.fetchall()