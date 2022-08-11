import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute(
    '''
    CREATE TABLE users
    (telegram_id int, name txt)
    '''
)
con.commit()
con.close