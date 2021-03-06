import sqlite3 as sql
from logsmith import log

# Connecting to DEV authLib Table
db = sql.connect("dataFiles/authLibProfiles_dev.db")

cursor = db.cursor()

# Create authProfiles Table in Test. SQL Statement
CREATE_TABLE_SQL_STATEMENT = '''
    DROP TABLE authProfiles_dev
'''

cursor.execute(CREATE_TABLE_SQL_STATEMENT)

CREATE_TABLE_SQL_STATEMENT = '''
    CREATE TABLE IF NOT EXISTS authProfiles_dev (
        email TEXT NOT NULL,
        authRequestID TEXT,
        name TEXT,
        passwordHash TEXT,
        hashedSecret TEXT,
        status TEXT,
        PRIMARY KEY (email)
    )
'''

cursor.execute(CREATE_TABLE_SQL_STATEMENT)

# Commit Changes to DB
db.commit()

# Log to console
log = log()
log.configure(console_only=False, ENV="Dev", logfile="logs")

log.SUCCESS("Auth Profiles Table Created!")