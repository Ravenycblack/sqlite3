import sqlite3

conn = sqlite3.connect("Demo.db")
cur = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS InfTable (
    fname TEXT,
    ename TEXT,
    epost STRING,
    tlf INTEGER,
    postnummer INTEGER,
    primary key(fname)
    ) """

cur.execute(sql)
print('Database has been created')

conn.commit()
conn.close()
