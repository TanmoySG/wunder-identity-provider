'''
Test Code - Will be changed later.
'''
import sqlite3 as sql

db = sql.connect("dataFiles/authLibProfiles.db")

cursor = db.cursor()

cursor.execute("CREATE TABLE authProfilesTest (id TEXT, name TEXT)")
cursor.execute("INSERT INTO authProfilesTest VALUES  ('1', 'T')")
cursor.execute("INSERT INTO authProfilesTest VALUES  ('2', 'S')")

db.commit()

for row in cursor.execute('SELECT * FROM authProfilesTest'):
    print(row)

db.close()