import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = 'CREATE TABLE users (id INTEGER PRIMARY KEY , username text, password text)'
cursor.execute(create_table)

create_table = 'create table items (id INTEGER PRIMARY KEY ,name text, price real)'
cursor.execute(create_table)

# cursor.execute('insert  into items values (?, ?)', ('piano', 12.01))

connection.commit()
connection.close()


