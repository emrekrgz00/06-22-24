import sqlite3

connection = sqlite3.connect("../database/Deneme.db")
cursor = connection.cursor()

videos = [['pacman', 17704, '2022-10-25'],
          ['read from text', 49677, '2021-12-29'],
          ['controls top 5', 15076, '2022-03-31'],
          ['python excel', 8037, '2022-05-19']]

for i in range(len(videos)):
    name = videos[i][0]
    views = videos[i][1]
    date = videos[i][2]
    cursor.execute('INSERT INTO sample VALUES (?, ?, ?)', (name, views, date))


# Must commit data or no changes will be saved
connection.commit()
connection.close()