import sqlite3

connection = sqlite3.connect("../database/Deneme.db")
cursor = connection.cursor()

cursor.execute('''DELETE FROM sample WHERE  vid_name="controls top 5";''')
connection.commit()

connection.close()
