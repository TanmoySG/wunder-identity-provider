import sqlite3 as sql

# Connecting to DEV authLib Table
db = sql.connect("dataFiles/authLibProfiles_dev.db")

cursor = db.cursor()

# Create authProfiles Table in Test.
CREATE_TABLE_SQL_STATEMENT = '''
    CREATE TABLE IF NOT EXISTS authProfiles (
        uID TEXT,
        email TEXT,
        timestamp TEXT,
        latestOTPHash TEXT,
        status TEXT
    )
'''

cursor.execute(CREATE_TABLE_SQL_STATEMENT)

db.commit()

for row in cursor.execute('SELECT COUNT(*) FROM authProfiles'):
    print(row)

db.close()
