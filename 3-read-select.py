import sqlite3

connection = sqlite3.connect("../database/Deneme.db")
cursor = connection.cursor()

# fetch all data from table in SQL db
cursor.execute("SELECT * FROM sample")
# store all fetched data inside results variable
results = cursor.fetchall()

for i in results:
    print(i)



connection.close()