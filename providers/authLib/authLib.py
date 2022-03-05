'''

'''
import sqlite3 as sql

db = sql.connect("dataFiles/test.db")

cursor = db.cursor()

cursor.execute("INSERT INTO testTable2 VALUES  (1, 'P')")
cursor.execute("INSERT INTO testTable2 VALUES  (2, 'S')")

db.commit()

for row in cursor.execute('SELECT * FROM testTable2'):
    print(row[0])

db.close()