import sqlite3

connection = sqlite3.connect("../database/Deneme.db")
cursor = connection.cursor()


cursor.execute('''UPDATE sample SET vid_name="python pacman" WHERE vid_name="pacman";''')
connection.commit()




connection.close()