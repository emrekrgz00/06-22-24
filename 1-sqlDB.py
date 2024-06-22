# Bir tablo ve database oluşturmak Python ile
import sqlite3

connection = sqlite3.connect("../database/Deneme.db")
cursor = connection.cursor()

# Each entry will have -- name, views, date(YYYY-MM-DD)
# sql command inside of triple quotes - MUST be written in SQL format

sql_command = """CREATE TABLE sample(
vid_name  VARCHAR(30),
view_count INTEGER,
published DATE
)"""

cursor.execute(sql_command)
connection.close()
