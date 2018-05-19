import sqlite3

conn = sqlite3.connect("basedatos.db") # or use :memory: to put it in RAM

cursor = conn.cursor()

# create a table
# cursor.execute("""CREATE TABLE albums
#                   (title text, artist text, release_date text,
#                    publisher text, media_type text)
#                """)

# insert some data
# cursor.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')")

# save data to database
conn.commit()

for row in cursor.execute('SELECT * FROM usuarios'):
        print(row)
