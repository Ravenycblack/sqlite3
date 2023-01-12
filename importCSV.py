import sqlite3

connection = sqlite3.connect("Demo.db")
cursor = connection.cursor()

with open('randoms.csv','r') as files:
    records = 0
    for row in files:
        cursor.execute("INSERT INTO InfTable VALUES (?,?,?,?,?)", row.split(","))
        connection.commit()
        records +=1
connection.close()
print('\n{} Records Transfer Completed'.format(records))